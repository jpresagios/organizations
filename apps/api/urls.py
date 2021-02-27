from django.urls import path
from .views.auth import ObtainAuthToken, GroupList
from .views.users import UserByOrganizationList, UserDetail
from .views.organizations import OrganizationDetail

urlpatterns = [
    path('auth/login/', ObtainAuthToken.as_view()),
    path('auth/groups/', GroupList.as_view()),

    path('users/', UserByOrganizationList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('organizations/<int:pk>/', OrganizationDetail.as_view()),
]
