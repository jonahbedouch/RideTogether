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
    return lat, long

# Create your views here.

class login_api_view(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        uinfo = UserSerializer(user)
        if user is not None:
            login(request, user)
            return Response(uinfo.data)
        else:
            return HttpResponse(status=400)

class register_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            "username": request.data.get("username"), 
            "email": request.data.get('email'),
            "password": request.data.get('password'),
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name')
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class logout_api_view(APIView):
    def post(self, request):
        logout(request)
        return HttpResponse(status=200)

class stalk_api_view(APIView):
    def post(self, request):
        uid = request.data.get('user_id')
        if request.user.id != uid:
            return HttpResponse(status=401)
        try:
            user = User.objects.get(id=uid)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return HttpResponse(status=400)


class session_start_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        driver = request.user.id
        long1, lat1 = [float(x) for x in request.data.get('origin')]
        long2, lat2 = [float(x) for x in request.data.get('dest')]
        timestart = int(request.data.get('timestart')) # epoch seconds
        passenger_max = int(request.data.get('passengers_max'))
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
        route = [latlong_to_bucket(x[1], x[0]) for x in nodes]
        print(route)
        data = {
            "driver": driver,
            "passenger_max": passenger_max, 
            "start_dest": [lat1, long1],
            "end_dest": [lat2, long2],
            "route": route,
            "passengers": [],
            "timestamp": timestart,
        }
        serializer = SessionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class session_end_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        pass

        

def trip_create(request):
    if request.user.is_authenticated and request.method == "POST":
        driver = request.user
        long1, lat1 = request.POST.get('origin')
        long2, lat2 = request.POST.get('dest')
        timestart = request.POST.get('timestart')
        passenger_max = request.POST.get('passenger_max')
        if not (36.96 < lat1 < 37.017) or not (-122.087 < long1 < -121.93):
            return JsonResponse({"status": 400, "message": "Origin must stay in Santa Cruz area."})
        if not (36.96 < lat2 < 37.017) or not (-122.087 < long2 < -121.93):
            return JsonResponse({"status": 400, "message": "Destination must stay in Santa Cruz area."})
        curtrip = Session()
        

def trip_details(request):
    pass

def trip_findlocal(request):
    pass

def test(request):
    if request.method == "POST":
        return JsonResponse({"status": 200})
    if request.method == "GET":
        return HttpResponse("Hello")




