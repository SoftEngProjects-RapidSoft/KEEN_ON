from django.shortcuts import render
from .models import Customer,Product, Order, Address


from .forms import CustomerUpdateForm, AddressUpdateForm, AddProductForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def account_details(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer#model.py
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        address, created = Address.objects.get_or_create(user= request.user)


    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'customer' : customer,'products':products, 'items':items, 'order': order, 'address':address}
    return render(request, 'store/account-details.html', context)



@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form = CustomerUpdateForm(request.POST, instance=request.user.customer)
        a_form = AddressUpdateForm(request.POST, instance=request.user.address)
        if u_form.is_valid():
            u_form.save()
            a_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('updateform')

    else:
        u_form = CustomerUpdateForm(instance=request.user.customer)
        a_form = AddressUpdateForm(instance=request.user.address) 

    context = {
        'u_form': u_form, 'a_form':a_form
    }

    return render(request, 'store/updateform.html', context)

@login_required
def addproduct(request):
    if request.method == 'POST':
        p_form = AddProductForm(request.POST or None)
        if p_form.is_valid():
            product = p_form.save(commit=False)
            product.customer = request.user.customer
            p_form.save()
            messages.success(request, f'New product has been added!')
            return redirect('account_details')
    else:
        p_form = AddProductForm()

    context = {
        'p_form':p_form
    }

    return render(request, 'store/addproductform.html', context)


def product_details(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/product-details.html', context)

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/index.html', context)

def account(request):
    context = {}
    return render(request, 'store/account.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer#model.py
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
