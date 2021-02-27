from rest_framework import serializers
from organization.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Organization
