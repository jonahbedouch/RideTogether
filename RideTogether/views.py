import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse

from .models import *

def latlong_to_bucket(lat, long):
    lat -= 36.94
    long -= -122.087
    lat //= 0.0075
    long //= 0.0075
    return lat, long

# Create your views here.


def index(request):
    pass

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return 
        else:
            return JsonResponse({
                "status": 400,
                "message": "Invalid email and/or password."
            })

def logout_view(request):
    logout(request)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError as e:
            print(e)
            return JsonResponse({
                "status": 400,
                "message": "Email address or username already taken."
            })
        login(request, user)
        userid = user.id
        return JsonResponse({
            "status": 200,
            "userid": userid
        })

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

def userdata(request):
    if request.method == "POST":
        user_id = int(request.POST.get('userid'))
        try: 
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"status": 400})
        return JsonResponse({
            "status": 200,
            "email": user.email,
            "username": user.username,
            "first_name": user.username,
            "last_name": user.last_name
        })

def test(request):
    if request.method == "POST":
        return JsonResponse({"status": 200})
    if request.method == "GET":
        return HttpResponse("Hello")




