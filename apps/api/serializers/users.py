from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from organization.models import Organization, OrganizationMember
from .organizations import OrganizationSerializer


class OrganizationMemberSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        fields = '__all__'
        model = OrganizationMember


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


class UserOrganizationSerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField()
    organization_id = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_organization_name(self, obj):
        return obj.organization.name

    def get_organization_id(self, obj):
        return obj.organization.pk

    def get_email(self, obj):
        return obj.user.email

    class Meta:
        fields = ('name', 'phone', 'birthdate', 'email', 'organization_name', 'organization_id')
        model = OrganizationMember
