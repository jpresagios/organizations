from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny

from api.serializers.users import OrganizationMemberSerializer, UserOrganizationSerializer, \
    UserCreateSerializer
from rest_framework.response import Response
from rest_framework import generics
from organization.models import OrganizationMember
from api.permissions import IsAdministratorOrViewer, AllowAnyForGET, IsAdminOrSameRequestUserForPATCH, \
    isAdminForDELETE
from rest_framework.exceptions import NotFound

import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_condition import Or
from api.views.search_util import get_search_conditions

class UserListCreate(APIView):
    permission_classes = (IsAdministratorOrViewer,)

    def get(self, request):
        """
        List all the users for the user organization if user is `Administrator` or
        `Viewer`. Must return all the user model fields. Should support search by name, email.
        Should support filter by phone
        """
        user = self.request.user

        organization = user.organization_member.organization

        query_search = get_search_conditions(self.request)
        
        if query_search:
            print(query_search)
            filtered = organization.members.filter(query_search)
            serializer = OrganizationMemberSerializer(filtered, many=True)
            return Response(serializer.data)
        

        serializer = OrganizationMemberSerializer(organization.members, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user

        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            email = request.data['email']
            password = request.data['password']

            new_user = User.objects.create_superuser(email, email, password)
            serializer.save(
                user=new_user,
                organization=user.organization_member.organization,
                birthdate=datetime.datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGetRetrieveDestroyUpdate(APIView):
    serializer_class = UserOrganizationSerializer

    permission_classes = (
        Or(AllowAnyForGET, IsAdminOrSameRequestUserForPATCH, isAdminForDELETE),)

    def get_object(self, pk):
        member = OrganizationMember.objects.filter(pk=pk).first()

        if not member:
            raise NotFound("User Id Not Found")

        return member

    def get(self, request, pk, format=None):
        organization_member = self.get_object(pk)

        serializer = UserOrganizationSerializer(organization_member)
        return Response(serializer.data)

    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)

        serializer = UserOrganizationSerializer(
            testmodel_object,
            data=request.data,
            partial=True)  # set partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)

        serializer = UserOrganizationSerializer(
            testmodel_object,
            data=request.data,
            partial=True)  # set partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
