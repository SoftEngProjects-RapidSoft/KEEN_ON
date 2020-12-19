
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import account_details, product_details, home 
from store.views import account, store, cart, checkout

# SimpleTestCase - not database related isues
class TestUrls(SimpleTestCase):

    def test_account_details_url_is_resolves(self):
        url = reverse('account_details')
        print(resolve(url))
        self.assertEquals(resolve(url).func, account_details)

    '''
    given en error
    def test_product_details_url_is_resolves(self):
        url = reverse('product_details')
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_details)
    '''

    def test_home_url_is_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_account_url_is_resolves(self):
        url = reverse('account')
        print(resolve(url))
        self.assertEquals(resolve(url).func, account)
    
    def test_store_url_is_resolves(self):
        url = reverse('store')
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_is_resolves(self):
        url = reverse('cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cart)
    
    def test_checkout_url_is_resolves(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

