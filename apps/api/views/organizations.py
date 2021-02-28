from api.serializers.organizations import OrganizationSerializer
from api.serializers.users import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from organization.models import Organization, OrganizationMember
from api.permissions import IsAdministratorOrViewer, IsAdministratorOrViewerForGET, IsAdministratorForPatch
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_condition import Or


class OrganizationRetrieveUpdateAPI(APIView):
    permission_classes = (Or(IsAdministratorOrViewerForGET, IsAdministratorForPatch),)

    def get_object(self, pk):
        return Organization.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        organization = self.get_object(pk)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)

    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)

        serializer = OrganizationSerializer(
            testmodel_object,
            data=request.data,
            partial=True)  # set partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationMemberList(APIView):
    permission_classes = (IsAdministratorOrViewer,)

    def get_object(self, pk):
        return Organization.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        organization = self.get_object(pk)
        members = organization.members

        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)


class OrganizationMemberDetail(APIView):
    permission_classes = (IsAdministratorOrViewer,)

    def get(self, request, pk, member_id, format=None):

        organization = Organization.objects.filter(pk=pk).first()
        member = OrganizationMember.objects.filter(
            organization=organization, pk=member_id).first()

        if not organization:
            return Response({'error': 'Organization not found'},
                            status=status.HTTP_400_BAD_REQUEST)

        if not member:
            return Response({'error': 'User not found'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(member)
        return Response(serializer.data)
