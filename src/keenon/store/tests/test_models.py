
from django.test import TestCase
from store.models import Address, Product, Order, OrderItem, ShippingAddress
from account.models import Customer
from django.contrib.auth.models import User


class TestAddress(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="nevzat",
                                    password="123",
                                    email="nevzatseferoglu@gmail.com",
                                    first_name="Nevzat",
                                    last_name="Seferoglu")
        country = "Turkey"
        city = "Tokat"
        town = "Merkez" 
        aveSt = "16st" 
        apartmentNo = "4"
        zipCode = "60100"
        
        cls.address = Address.objects.create(user=user,
                                        country=country, city=city, town=town, 
                                        aveSt=aveSt, apartmentNo=apartmentNo, zipCode=zipCode)

    def test_Adress_is_not_none(self):
        return self.assertNotEqual(self.address, None)

class TestProduct(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="nevzat",
                                    password="123",
                                    email="nevzatseferoglu@gmail.com",
                                    first_name="Nevzat",
                                    last_name="Seferoglu")
        image = None
        phone = f"5549097411"
        customer = Customer.objects.create(user=user, image=image, phone=phone)

        name = "Elisi Kazak"
        price = 12.15 
        digital = False
        image = None
        quantity = 2
        description = f"el ile yapilmis kazak"
        
        cls.product = Product.objects.create(customer=customer, name=name, price=price, 
                            digital=digital, image=image, quantity=quantity, description=description)
        
    def test_Product_is_not_none(self):
        return self.assertNotEqual(self.product, None)

class TestOrder(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="nevzat",
                                    password="123",
                                    email="nevzatseferoglu@gmail.com",
                                    first_name="Nevzat",
                                    last_name="Seferoglu")
        image = None
        phone = f"5549097411"
        customer = Customer.objects.create(user=user, image=image, phone=phone)

        data_ordered = None
        complete = False
        transaction_id = 45923
        
        cls.order = Order.objects.create(customer=customer,
                                        data_ordered=data_ordered, transaction_id=transaction_id)

    def test_Order_is_not_none(self):
        return self.assertNotEqual(self.order, None)

class TestOrderItem(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="nevzat",
                                    password="123",
                                    email="nevzatseferoglu@gmail.com",
                                    first_name="Nevzat",
                                    last_name="Seferoglu")
        image = None
        phone = f"5549097411"
        customer = Customer.objects.create(user=user, image=image, phone=phone)

        name = "Elisi Kazak"
        price = 12.15 
        digital = False
        image = None
        quantity = 2
        description = f"el ile yapilmis kazak"
        
        cls.product = Product.objects.create(customer=customer, name=name, price=price, 
                            digital=digital, image=image, quantity=quantity, description=description)

        data_ordered = None
        complete = False
        transaction_id = 45923
        
        cls.order = Order.objects.create(customer=customer,
                                        data_ordered=data_ordered, transaction_id=transaction_id)

        quantity = 4
        date_added = None

        cls.orderItem = OrderItem.objects.create(product=cls.product, order=cls.order, quantity=quantity, 
                                        date_added=date_added)

    def test_OrderItem_is_not_none(self):
        return self.assertNotEqual(self.orderItem, None)