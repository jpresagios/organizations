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
from .comparator_utils import comparate_organization


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        generate_all()

    def user_group_name(self, group_name):
        url_login = reverse('login')
        url_user_organization = reverse('user_organization_members')

        for user in User.objects.filter(groups__name=group_name):

            response = self.client.post(url_login,
                                        {'email': user.email, 'password': 'admin123'},
                                        format='json')
            token = response.data['token']

            response = self.client.get(url_user_organization,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            self.assertEqual(response.status_code, 200)
            user_organization = user.organization_member.organization
            self.assertEqual(response.status_code, 200)

            user_organization_members = user.organization_member.organization.members

            # The users organizations members len is equal to response
            self.assertEqual(user_organization_members.count(), len(response.data))

    def organization_detail_group(self, group):
        user = User.objects.filter(groups__name=group).first()
        token = get_token(user)

        for organization in Organization.objects.all():
            url_detail_organization = reverse('organization_retrieve_update', args=[organization.pk])

            response = self.client.get(url_detail_organization,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            # Validate status code response
            self.assertEqual(response.status_code, 200)

            org_comp = comparate_organization(organization, response.data)
            self.assertEqual(org_comp, True)

    def test_organization_detail_admin(self):
        """
        GET /api/organizations/{id}/
        Retrieve organization information if request user is `Administrator`
        """

        self.organization_detail_group('Administrator')

    def test_organization_detail_viewer(self):
        """
        GET /api/organizations/{id}/
        Retrieve organization information if request user is `Viewer`
        """

        self.organization_detail_group('Viewer')

    def test_organization_detail_user(self):
        """
        GET /api/organizations/{id}/
        Retrieve organization information if request user is `User` should return 403
        """

        user = User.objects.filter(groups__name='User').first()
        token = get_token(user)

        for organization in Organization.objects.all():
            url_detail_organization = reverse('organization_retrieve_update', args=[organization.pk])

            response = self.client.get(url_detail_organization,
                                       HTTP_AUTHORIZATION=f"JWT {token}",
                                       format='json')

            self.assertEqual(response.status_code, 403)

    def test_organization_patch(self):
        """
        PATCH /api/organizations/{id} Update organization if request user is `Administrator`.
        """

        user = User.objects.filter(groups__name='Administrator').first()
        token = get_token(user)

        for organization in Organization.objects.all():
            url_patch_organization = reverse('organization_retrieve_update', args=[organization.pk])

            patch_name = f"{organization.name}-newname"
            response = self.client.patch(url_patch_organization,
                                         data={'name': patch_name},
                                         HTTP_AUTHORIZATION=f"JWT {token}",
                                         format='json')

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['name'], patch_name)

    def test_organization_patch_not_admin(self):
        """
        PATCH /api/organizations/{id} Update organization if request user is not `Administrator`
        should return 403
        """

        user = User.objects.filter(~Q(groups__name='Administrator')).first()
        token = get_token(user)

        for organization in Organization.objects.all():
            url_patch_organization = reverse('organization_retrieve_update', args=[organization.pk])

            patch_name = f"{organization.name}-newname"
            response = self.client.patch(url_patch_organization,
                                         data={'name': patch_name},
                                         HTTP_AUTHORIZATION=f"JWT {token}",
                                         format='json')

            self.assertEqual(response.status_code, 403)
