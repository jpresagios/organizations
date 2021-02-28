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


class UserSearchTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        generate_all()

    def test_search_by_phone(self):
        """
        GET /api/users/ List all the users for the user organization if user is `Administrator` or
        `Viewer`. Must return all the user model fields. Should support search by name, email.
        Should support filter by phone.
        """

        for user in User.objects.filter(Q(groups__name='Administrator') | Q(
                groups__name='Viewer')):

            token = get_token(user)

            url_search_by_phone = f"{reverse('user_organization_members')}?phone={user.organization_member.phone}"

            response = self.client.get(url_search_by_phone,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            self.assertEqual(response.status_code, 200)

            for data in response.data:
                self.assertEqual(user.organization_member.phone, data['phone'])

    def test_search_by_name(self):
        """
        GET /api/users/ List all the users for the user organization if user is `Administrator` or
        `Viewer`. Must return all the user model fields. Should support search by name, email.
        Should support filter by phone.
        """

        for user in User.objects.filter(Q(groups__name='Administrator') | Q(
                groups__name='Viewer')):

            token = get_token(user)

            url_search_by_phone = f"{reverse('user_organization_members')}?name={user.organization_member.name}"

            response = self.client.get(url_search_by_phone,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            self.assertEqual(response.status_code, 200)

            for data in response.data:
                self.assertEqual(user.organization_member.name, data['name'])

    def test_search_by_email(self):
        """
        GET /api/users/ List all the users for the user organization if user is `Administrator` or
        `Viewer`. Must return all the user model fields. Should support search by name, email.
        Should support filter by phone.
        """

        for user in User.objects.filter(Q(groups__name='Administrator') | Q(
                groups__name='Viewer')):

            token = get_token(user)

            url_search_by_phone = f"{reverse('user_organization_members')}?email={user.organization_member.name}"

            response = self.client.get(url_search_by_phone,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            self.assertEqual(response.status_code, 200)

            for data in response.data:
                self.assertEqual(user.organization_member.email, data['email'])
