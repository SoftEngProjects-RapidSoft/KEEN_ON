
from django.test import TestCase, Client
from django.urls import reverse
from store.models import Customer, Product, Order, OrderItem, ShippingAddress
import json


# path url name ile html file in ismini ayni yapsakdik
# daha guzel olurmus

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.account_details_url = reverse('account_details')
        #self.product_details_url = reverse('product_details')
        self.account_url = reverse('account')
        self.store_url = reverse('store')
        self.cart_url = reverse('cart')
        self. checkout_url = reverse('checkout')

    def test_account_details_GET(self):
        response = self.client.get(self.account_details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/account-details.html')
    
    '''
    erroneous test
    def test_product_details_GET(self):
        response = self.client.get(self.product_details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/product_details_url.html')
    '''
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_account_url_is_resolves(self):
        response = self.client.get(self.account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/account.html')

    def test_store_GET(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')

    def test_cart_GET(self):
        response = self.client.get(self.cart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')

    def test_cart_GET(self):
        response = self.client.get(self.checkout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')

    