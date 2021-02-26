from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from api.serializers import OrganizationMemberSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import Group
from organization.models import OrganizationMember
from api.permissions import IsAdministratorOrViewer


class UserByOrganizationList(generics.ListAPIView):
    permission_classes = (IsAdministratorOrViewer,)
    serializer_class = OrganizationMemberSerializer

    def get_queryset(self):
        """
        List all the users for the user organization if user is `Administrator` or
        `Viewer`. Must return all the user model fields. Should support search by name, email.
        Should support filter by phone
        """
        user = self.request.user

        organization = user.organization_member.organization

        return organization.members
