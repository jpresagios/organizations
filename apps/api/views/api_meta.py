from rest_framework import generics
from django.contrib.auth.models import User
from organization.models import Organization, OrganizationMember
from api.permissions import IsAdministratorOrViewer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from api.serializers.meta_serializers import ApiInfoSerializer
import socket

class ApiInfo(APIView):

    def get(self, request):
        user = request.user

        serializer = ApiInfoSerializer({'user_name': user.email,
                                        'id': user.pk,
                                        'organization_name': user.organization_member.organization,
                                        'public_ip': socket.gethostbyname(socket.getfqdn())})

        return Response(data=serializer.data, status=200)
