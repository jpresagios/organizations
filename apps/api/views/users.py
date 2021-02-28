from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny
from api.serializers.users import OrganizationMemberSerializer, UserOrganizationSerializer
from rest_framework.response import Response
from rest_framework import generics
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


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserOrganizationSerializer
    queryset = OrganizationMember.objects.all()
