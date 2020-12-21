from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
	path('', views.account, name="account"),
	path('details/', views.account_details, name = "account_details"),
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
]
