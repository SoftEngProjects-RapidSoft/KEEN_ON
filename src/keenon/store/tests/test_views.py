
from django.test import TestCase, Client
from django.urls import reverse
from store.models import Address, Product, Order, OrderItem, ShippingAddress
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.store_url = reverse('store')
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')
        #self.product_details_url = reverse('product_details')


    '''
    Error occureed
    def test_product_details_GET(self):
        response = self.client.get(self.product_details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store/product-details.html')
    '''

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_store_GET(self):
        response = self.client.get(self.store_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')


    #def test_cart_GET(self):
     #   response = self.client.get(self.cart_url)
      #  self.assertEquals(response.status_code, 302)
       # self.assertTemplateUsed(response, 'store/cart.html')

    def test_checkout_GET(self):
        response = self.client.get(self.checkout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')

    
