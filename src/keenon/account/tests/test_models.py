
from django.test import TestCase
from account.models import Customer
from django.contrib.auth.models import User


class TestCustomer(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="nevzat",
                                    password="123",
                                    email="nevzatseferoglu@gmail.com",
                                    first_name="Nevzat",
                                    last_name="Seferoglu")
        image = None
        phone = f"5549097411"
        cls.customer = Customer.objects.create(user=user, image=image, phone=phone)
        
    def test_Customer_is_not_none(self):
        return self.assertNotEqual(self.customer, None)
