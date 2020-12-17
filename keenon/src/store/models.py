from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User,null=True, blank=True, on_delete= models.CASCADE)
	userName = models.CharField(max_length= 200, null=True)
	email = models.CharField(max_length= 200)
	firstName = models.CharField(max_length= 200, null=True)
	lastName = models.CharField(max_length= 200, null=True)
	#image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	phone =  models.CharField(max_length= 12, null=True)
	

	def _str_(self):
		return self.userName

class Address(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
	country =models.CharField(max_length= 200, null=True) 
	city =models.CharField(max_length= 200, null=True)
	town =models.CharField(max_length= 200, null=True) 
	aveSt = models.CharField(max_length= 200, null=True) 
	apartmentNo = models.CharField(max_length= 200, null=True) 
	zipCode = models.CharField(max_length= 200, null=True) 
		
	def _str_(self):
		return self.country + " " + self.city + " " + self.town + " " +self.aveSt + " " + self.apartmentNo + " " + self.zipCode		

class Product(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	price= models.FloatField()
	digital = models.BooleanField(default=False, null=True, blank=False)
	image = models.ImageField(null=True, blank=True)

	def _str_(self):
		return self.name
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	data_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def _str_(self):
		return str(self.id)
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price *self.quantity
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.address
