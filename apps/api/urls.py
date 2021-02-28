from django.urls import path
from .views.auth import ObtainAuthToken, GroupList
from .views.users import UserByOrganizationList, UserGetRetrieveDestroyUpdate
from .views.organizations import OrganizationRetrieveUpdateAPI, OrganizationMemberList, \
        OrganizationMemberDetail

urlpatterns = [
    path('auth/login/', ObtainAuthToken.as_view(), name="login"),
    path('auth/groups/', GroupList.as_view(), name='auth_groups'),

    path('users/', UserByOrganizationList.as_view(), name='user_organization_members'),
    path('users/<int:pk>/', UserGetRetrieveDestroyUpdate.as_view(), name="user_get_retrieve_destroy_update"),

    path('organizations/<int:pk>/', OrganizationRetrieveUpdateAPI.as_view(), name="organization_retrieve_update"),
    path('organization/<int:pk>/users/', OrganizationMemberList.as_view(), name="organization_members"),
    path('organization/<int:pk>/users/<int:member_id>/', OrganizationMemberDetail.as_view(), name="organization_members"),

]
