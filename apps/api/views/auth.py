from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from api.serializers import AuthSerializer
from rest_framework.response import Response


class ObtainAuthToken(APIView):

    permission_classes = ()

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
