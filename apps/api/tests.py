import pdb
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from organization.models import OrganizationMember, Organization
from django.contrib.auth.models import User, Group
from django.db.models import Q
from api.fake import generate_all


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


    
    def test_list_user_organization_admin(self):
        """
        GET /api/users/ List all the users for the user organization if user is `Administrator` or `Viewer`
        This test is for user in Administrator Group
        """

        self.user_group_name('Administrator')


    def test_list_user_organization_viewer(self):
        """
        GET /api/users/ List all the users for the user organization if user is `Administrator` or `Viewer`
        This test is for user in Viewer Group
        """

        self.user_group_name('Viewer')


    def test_list_user_organization_user(self):
        """
        GET /api/users/ List all the users for the user organization if user is `Administrator` or `Viewer`
        This test is for user that don't belong to Administrator or Viewer
        """

        url_login = reverse('login')
        url_user_organization = reverse('user_organization_members')

        for user in User.objects.filter(~Q(groups__name='Administrator')&~Q(groups__name='Viewer')):
            response = self.client.post(url_login,
                                        {'email': user.email, 'password': 'admin123'},
                                        format='json')
                            
            token = response.data['token']
            response = self.client.get(url_user_organization, 
                                        HTTP_AUTHORIZATION=f"JWT {token}", 
                                        format='json')

            self.assertEqual(response.status_code, 403)