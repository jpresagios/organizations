from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from organization.models import Organization, OrganizationMember












