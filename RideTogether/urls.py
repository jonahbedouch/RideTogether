from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_api_view.as_view(), name="login"),
    path("logout", views.logout_api_view.as_view(), name="logout"),
    path("register", views.register_api_view.as_view(), name="register"),
    path("stalk", views.stalk_api_view.as_view(), name="stalk"),
    path("start", views.session_start_api_view.as_view(), name="start"),
]