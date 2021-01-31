
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time

class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'functional_tests\chromedriver.exe')
    
    def tearDown(self):
        self.browser.close()

    def test_store_main_url_request(self):
        self.browser.get('http://localhost:8000/')
        self.browser.implicitly_wait(1)

    def test_store_store_url_request(self):
        self.browser.get('http://localhost:8000/store/')
        self.browser.implicitly_wait(1)
    
    def test_store_cart_url_request(self):
        self.browser.get('http://localhost:8000/cart/')
        self.browser.implicitly_wait(1)
    
    def test_store_checkout_url_request(self):
        self.browser.get('http://localhost:8000/checkout/')
        self.browser.implicitly_wait(1)

    def test_store_update_item_url_request(self):
        self.browser.get('http://localhost:8000/update_item/')
        self.browser.implicitly_wait(1)
    
    def test_store_process_order_url_request(self):
        self.browser.get('http://localhost:8000/process_order/')
        self.browser.implicitly_wait(1)
    
    def test_store_product_details_url_request(self):
        self.browser.get('http://localhost:8000/product_details/')
        self.browser.implicitly_wait(1)