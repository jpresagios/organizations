from django.urls import path
from .views.auth import ObtainAuthToken

urlpatterns = [
    path('auth/login/', ObtainAuthToken.as_view()),
]
