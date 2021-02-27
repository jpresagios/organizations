from api.serializers.organizations import OrganizationSerializer
from rest_framework import generics
from organization.models import Organization
from api.permissions import IsAdministratorOrViewer


class OrganizationDetail(generics.RetrieveAPIView):
    permission_classes = (IsAdministratorOrViewer,)
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
