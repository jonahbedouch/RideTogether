from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("stupid", views.test_api_view.as_view(), name="test")
]