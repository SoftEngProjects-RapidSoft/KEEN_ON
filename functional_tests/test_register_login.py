
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time

class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'functional_tests\chromedriver.exe')
    
    def tearDown(self):
        self.browser.close()


    def test_register_and_login(self):
        self.browser.get('http://localhost:8000/account/login/')

        name                = f"Ahmet"
        lastname            = f"Umit"
        username            = f"ahmet1457"
        email               = f"ahmet1457@gmail.com"
        phone_number        = f"8674929"
        password            = f"Ahmetumit+1."
        verified_password   = f"Ahmetumit+1"
        
        name_p              = self.browser.find_element_by_name("first_name")
        lastname_p          = self.browser.find_element_by_name("last_name")
    
        username_p          = self.browser.find_element_by_id("username2")
        email_p             = self.browser.find_element_by_name("email")
        phone_number_p      = self.browser.find_element_by_name("phone")
        password_p          = self.browser.find_element_by_name("password1")
        verified_password_p = self.browser.find_element_by_name("password2")
        time.sleep(2)
        
        # sending inputs to register page
        name_p.clear()
        name_p.send_keys(name)

        lastname_p.clear()
        lastname_p.send_keys(lastname)

        username_p.clear()
        username_p.send_keys(username)

        email_p.clear()
        email_p.send_keys(email)

        phone_number_p.clear()
        phone_number_p.send_keys(phone_number)

        password_p.clear()
        password_p.send_keys(password)

        verified_password_p.clear()
        verified_password_p.send_keys(verified_password)

        register_btn = self.browser.find_element_by_id("btn2")
        register_btn.click()
        time.sleep(1)

        '''
        # login with registered account
        username_ = self.browser.find_element_by_id("username1")
        password_ = self.browser.find_element_by_id("password3")
                
        #username_.clear()
        username_.send_keys("bhb1")

        #password_.clear()
        password_.send_keys("bhb1234")

        login_btn = self.browser.find_element_by_id("btn1")
        login_btn.click()
        '''