from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
	path('', views.account, name="account"),
	path('details/', views.account_details, name = "account-details"),
	path('addproductform/', views.addproduct, name = "addproductform"),
	path('updateform/', views.profile, name = "updateform"),
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
]
