from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', )
        model = Group


class AuthSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user_request = get_object_or_404(
                User,
                email=email,
            )
            user = authenticate(username=user_request.username, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs
