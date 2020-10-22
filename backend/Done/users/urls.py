from django.urls import path, include
from .api import RegisterAPI, UserAPI, LoginAPI

urlpatterns = [
    path('auth/', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/signin', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view())
]