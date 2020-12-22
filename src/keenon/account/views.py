from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateCostumerForm,CustomerUpdateForm, AddressUpdateForm, AddProductForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .models import Customer
from store.models import Product,Address

# Create your views here.
def account_details(request):
	products = Product.objects.all()
	if request.user.is_authenticated:
		customer = request.user.customer#model.py
		#order, created = Order.objects.get_or_create(customer=customer, complete=False)
		#items= order.orderitem_set.all()
		address, created = Address.objects.get_or_create(user= request.user)
		user = request.user
		products = Product.objects.filter(customer=request.user.customer)

	else:
		pass
		#items = []
		#order = {'get_cart_total':0, 'get_cart_items':0}
	context = {'customer' : customer,'products':products, 'address':address, 'user':user, 'products':products}
	return render(request, 'account/account-details.html', context)
	
@login_required
def profile(request):
	
	if request.method == 'POST':
		u_form = CustomerUpdateForm(request.POST,request.FILES, instance=request.user.customer)
		a_form = AddressUpdateForm(request.POST, instance=request.user.address)
		uu_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid() and uu_form.is_valid():
			u_form.save()
			a_form.save()
			uu_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('account:account-details')

	else:
		uu_form = UserUpdateForm(instance=request.user)
		u_form = CustomerUpdateForm(instance=request.user.customer)
		a_form = AddressUpdateForm(instance=request.user.address) 

	context = {
		'u_form': u_form, 'a_form':a_form, 'uu_form':uu_form
	}

	return render(request, 'account/updateform.html', context)

@login_required
def addproduct(request):
	if request.method == 'POST':
		p_form = AddProductForm(request.POST or None, request.FILES)
		if p_form.is_valid():
			product = p_form.save(commit=False)
			product.customer = request.user.customer
			p_form.save()
			messages.success(request, f'New product has been added!')
			return redirect('account:account-details')
	else:
		p_form = AddProductForm()

	context = {
		'p_form':p_form
	}

	return render(request, 'account/addproductform.html', context)

def account(request):
	if request.user.is_authenticated:
		return redirect('account:account-details')

	form_user = CreateUserForm()
	form_customer = CreateCostumerForm()
	context = {'form_user':form_user , 'form-customer':form_customer}
	return render(request, 'account/login-register.html', context)

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	if request.method == "POST":
		print("HERE", request.POST.get('username'))
		created_user_form = CreateUserForm(request.POST)
		created_customer_form = CreateCostumerForm(request.POST)
		if created_user_form.is_valid() and created_customer_form.is_valid():
			new_user = created_user_form.save()
			new_customer = created_customer_form.save(commit=False)
			new_customer.user = new_user
			created_customer_form.save()
			messages.success(request, 'Account was created for ' + new_user.username)
			return redirect('account:login')
		else:
			messages.info(request, 'Invalid register form')

	form_user = CreateUserForm()
	form_customer = CreateCostumerForm()
	context = {'form_user':form_user , 'form_customer':form_customer}
	return render(request, 'account/login-register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if(user is not None):
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'account/login-register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('account:login')
