from django.shortcuts import render
from .models import Product, Order
from account.views import account_details, login
from account.models import Customer
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
# Create your views here.

def product_details(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/product-details.html', context)

def home(request):
	products = Product.objects.all().order_by('-id')[:6]
	context = {'products':products}
	return render(request, 'store/index.html', context)

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products': products, 'cartItems': cartItems}
	return render(request, 'store/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		return redirect( "account:login")
		#Create empty cart for now for non-logged in user

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		if (request.user.address.country==None or request.user.address.city==None or request.user.address.town==None or request.user.address.aveSt==None or request.user.address.apartmentNo==None):
			messages.warning(request, 'You need to update your address information from Account Page->Edit User Information')
			context = {'messages':messages,'items':items, 'order':order, 'cartItems':cartItems}
			return redirect('cart')
		address=request.user.address

	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']
		address = None
	context = {'items':items, 'order':order, 'cartItems':cartItems,'address':address}
	return render(request, 'store/checkout.html', context)
 
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	print("HERE")
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		if not(orderItem.quantity+1 > product.quantity):
			orderItem.quantity = (orderItem.quantity + 1)
			product.quantity-=1
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
		product.quantity+=1

	product.save()
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	print("HERE2")
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
def product_details(request,id):
	context = {}
	product = get_object_or_404(Product,id = id)
	context = {'product': product, 'id': id}
	print(product.quantity)
	return render(request, "store/product-details.html",context)


# these are all just for GET request, POST tests will be 
# added soon
