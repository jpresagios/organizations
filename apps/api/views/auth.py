from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from api.serializers import AuthSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import Group
from drf_yasg.utils import swagger_auto_schema


class GroupList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ObtainAuthToken(APIView):
    permission_classes = ()

    @swagger_auto_schema(request_body=AuthSerializer, responses={200: "token"})
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        content = {
            'token': str(token),
        }

        return Response(content)
