from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateCostumerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Customer

# Create your views here.
def account_details(request):
	customer = Customer.objects.all()
	context = {'customer' : customer}
	return render(request, 'account/account-details.html', context)

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
