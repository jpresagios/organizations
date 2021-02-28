from rest_framework.test import APIClient
from django.urls import reverse

def get_token(user):
    client = APIClient()

    url_login = reverse('login')
    response = client.post(url_login, {'email': user.email, 
                                       'password': 'admin123'},
                                        format='json')
    token = response.data['token']
    return token