from api.serializers.organizations import OrganizationSerializer
from rest_framework import generics
from organization.models import Organization
from api.permissions import IsAdministratorOrViewer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status


class OrganizationDetail(APIView):
    permission_classes = (IsAdministratorOrViewer,)

    def get_object(self, pk):
        return Organization.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        organization = self.get_object(pk)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)
