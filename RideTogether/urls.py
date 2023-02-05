from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", views.login_api_view.as_view(), name="login"),
    path("logout/", views.logout_api_view.as_view(), name="logout"),
    path("register/", views.register_api_view.as_view(), name="register"),
    path("stalk/", views.stalk_api_view.as_view(), name="stalk"),
    path("start/", views.session_start_api_view.as_view(), name="start"),
    path("find/", views.session_find_api_view.as_view(), name="find"),
    path("api-token-auth/", obtain_auth_token, name='api_token_auth'),
    path("join/", views.session_join_api_view.as_view(), name="join"),
    path("check-requests/", views.check_waitlist_api_view.as_view(), name="check-request"),
    

]