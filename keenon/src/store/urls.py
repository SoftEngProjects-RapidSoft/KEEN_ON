from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
    path('', views.home, name="home"),
    path('account_details/', views.account_details, name = "account_details"),
	path('updateform/', views.profile, name = "updateform"),
	path('store/', views.store, name="store"),
	path('account/', views.account, name="account"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]