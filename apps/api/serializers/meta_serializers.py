from rest_framework import serializers

class ApiInfoSerializer(serializers.Serializer):    
    user_name = serializers.CharField()
    id = serializers.IntegerField()
    organization_name = serializers.CharField()
    public_ip = serializers.CharField()