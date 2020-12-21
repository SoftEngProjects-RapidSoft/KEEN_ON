from django.shortcuts import render
from .models import Product, Order
from account.models import Customer

# Create your views here.

def product_details(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/product-details.html', context)

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/index.html', context)

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


# these are all just for GET request, POST tests will be 
# added soon