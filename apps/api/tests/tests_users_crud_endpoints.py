import pdb
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from organization.models import OrganizationMember, Organization
from django.contrib.auth.models import User, Group
from django.db.models import Q
from api.fake import generate_all
from .tokens import get_token
from .comparator_utils import comparator_member


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        generate_all()

    def test_detail_user(self):
        """
        GET /api/organization/{id}/users List all the users for the user organization if user is
        `Administrator`
        """
        
        for user in User.objects.filter(Q(groups__name='Administrator') | Q(
                groups__name='Viewer') | Q(groups__name='User')):

            token = get_token(user)

            url_detail_user = reverse(
                'user_get_retrieve_destroy_update', args=[user.organization_member.pk])

            response = self.client.get(url_detail_user,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            # Validate status code response
            self.assertEqual(response.status_code, 200)

            org_comp = comparator_member(user.organization_member, response.data)
            self.assertEqual(org_comp, True)
