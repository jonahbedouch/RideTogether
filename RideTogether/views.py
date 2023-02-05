import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import *
import requests
import datetime

from .models import *

def latlong_to_bucket(lat, long):
    lat -= 36.94
    long -= -122.087
    lat = int(lat//0.0075)
    long = int(long//0.0075)
    return [lat, long]

# Create your views here.

class login_api_view(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        uinfo = UserSerializer(user)
        if user is None:
            return HttpResponse(status=400)
        login(request, user)
        return Response(uinfo.data)

class register_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            "username": request.data.get("username"), 
            "email": request.data.get('email'),
            "password": request.data.get('password'),
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get("last_name"),
            "phone_number": request.data.get('phone_number')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                user = serializer.create(data)
                user.save()
            except IntegrityError as e:
                print(e)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class logout_api_view(APIView):
    def post(self, request):
        logout(request)
        return HttpResponse(status=200)

class stalk_api_view(APIView):
    def post(self, request):
        uid = int(request.data.get('user_id'))
        print(request.user.id, uid)
        #if request.user.id != uid:
        #    return HttpResponse(status=401)
        try:
            user = User.objects.get(id=uid)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return HttpResponse(status=400)


class session_start_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        driver = request.user.id
        origin = request.data.get('origin')
        dest = request.data.get('dest')
        key = "de8151350cacbf98bdcabeb713955ca0"
        originresponse = requests.get(f"http://api.positionstack.com/v1/forward?access_key={key}&query={'%20'.join(origin.split())}").json()['data'][0]
        destresponse = requests.get(f"http://api.positionstack.com/v1/forward?access_key={key}&query={'%20'.join(dest.split())}").json()['data'][0]
        long1, lat1 = originresponse['longitude'], originresponse['latitude']
        long2, lat2 = destresponse['longitude'], destresponse['latitude']
        timestart = int(request.data.get('timestart')) # epoch seconds
        passengers_max = int(request.data.get('passengers_max'))
        if not (36.96 < lat1 < 37.017) or not (-122.087 < long1 < -121.93):
            return HttpResponse("Origin must be in SC", status=403)
        if not (36.96 < lat2 < 37.017) or not (-122.087 < long2 < -121.93):
            return HttpResponse("Destination must be in SC", status=403)
        key = "pk.eyJ1Ijoia3lsZTUxOCIsImEiOiJjbGRxNTZpcGQwcnFzM29wNjdyaXNiNzBuIn0.w43yIma1qixEO7je9gVSJQ"
        profile = "mapbox/driving"
        coordinates = fr"{long1}%2C{lat1}%3B{long2}%2C{lat2}"
        link = f"https://api.mapbox.com/directions/v5/{profile}/{coordinates}?alternatives=false&geometries=geojson&overview=simplified&steps=false&access_token={key}"
        print(link)
        response = requests.get(link)
        nodes = response.json()['routes'][0]['geometry']['coordinates']
        # timeend could be implemented in future, but not worth it because we're only operating in santa cruz
        route = [latlong_to_bucket(x[1], x[0]) for x in nodes]
        data = {
            "driver": driver,
            "passengers_max": passengers_max, 
            "start_dest": [lat1, long1],
            "end_dest": [lat2, long2],
            "original_route": nodes,
            "route": route,
            "passengers": {"passenger_ids": []},
            "timestamp": timestart,
            "joinqueue": {"joinqueue": []}
        }
        serializer = SessionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class session_find_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        origin = request.data.get('origin')
        dest = request.data.get('dest')
        key = "de8151350cacbf98bdcabeb713955ca0"
        originresponse = requests.get(f"http://api.positionstack.com/v1/forward?access_key={key}&query={'%20'.join(origin.split())}").json()['data'][0]
        destresponse = requests.get(f"http://api.positionstack.com/v1/forward?access_key={key}&query={'%20'.join(dest.split())}").json()['data'][0]
        long1, lat1 = originresponse['longitude'], originresponse['latitude']
        long2, lat2 = destresponse['longitude'], destresponse['latitude']
        timestart = int(request.data.get('timestart')) # epoch seconds
        peopleamt = int(request.data.get('people_amt'))
        print(timestart, peopleamt)
        print(Session.objects.all())
        possible = Session.objects.exclude(passengers_max=0)
        origin = latlong_to_bucket(lat1, long1)
        possible = [x for x in possible if (timestart - 3600 < x.timestamp < timestart + 3600) and (x.passengers_max-peopleamt >=0)]
        dest = latlong_to_bucket(lat2, long2)
        print(possible)
        print(origin, dest)
        res = []
        for i in possible:
            try:
                j = i.route.index(origin)
                if dest in i.route[j+1:]:
                    res.append(i)
            except ValueError:
                pass
        res = [PublicSessionSerializer(x).data for x in res]
        return Response({"sessions": res})

class session_join_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        passenger = request.user
        session_id = int(request.data.get('session_id'))
        session = Session.objects.get(id=session_id)
        session.joinqueue['joinqueue'].append(passenger.id)
        return Response(PublicSessionSerializer(session).data)
    
class check_waitlist_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        # only for drivers, poll 
        driver = request.user
        try:
            session = Session.objects.get(driver=driver)
            return Response(session.joinqueue)
        except Session.DoesNotExist:
            return HttpResponse(status=400)

class waitlist_drop_api_view(APIView):
    ## IN PROG
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        driver = request.user
        dropped_user_id = request.data.get("dropped_user_id")
        try:
            session = Session.objects.get(driver=driver)
            return Response([UserSerializer(x).data for x in session.joinqueue.all()])
        except Session.DoesNotExist:
            return HttpResponse(status=400)

class session_end_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        pass


        




