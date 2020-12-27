
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import home, store, cart, checkout

# SimpleTestCase - not database related isues

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_store_url_is_resolves(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_is_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)
    
    def test_checkout_url_is_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

