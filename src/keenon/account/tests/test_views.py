from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from account.models import Customer
'''
class TestRegister(TestCase):
    def setUp(self):
        user = User.objects.create(username="nevzat",
                                    password="123",
                                    email="nevzatseferoglu@gmail.com",
                                    first_name="Nevzat",
                                    last_name="Seferoglu")
        

    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
'''