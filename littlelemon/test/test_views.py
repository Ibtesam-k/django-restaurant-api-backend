from django.test import TestCase, Client
from restaurant.models import Menu
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
     def setUp(self):
        self.model_instance = Menu.objects.create(title="Chocolate", price=70, inventory=78)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
     def test_getall(self):
         client = Client()
         headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}

         response = client.get('/api/menu-items/',**headers)

         self.assertEqual(response.status_code, 200)

         serializer = MenuSerializer(self.model_instance)
         self.assertEqual(response.data, [serializer.data])

         
        