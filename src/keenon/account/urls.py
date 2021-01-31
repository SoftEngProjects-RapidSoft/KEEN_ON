from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account'

urlpatterns = [
	path('', views.account, name="account"),
	path('details/', views.account_details, name = "account-details"),
	path('addproductform/', views.addproduct, name = "addproductform"),
	path('updateform/', views.profile, name = "updateform"),
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),

	path('reset_password/', auth_views.PasswordResetView.as_view(
		email_template_name="account/password_reset_email.html",
		success_url=reverse_lazy("account:password_reset_done"),
		template_name = "account/password_reset.html"), name="reset_passwod"),

	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
		template_name="account/password_reset_sent.html"), name="password_reset_done"),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
		success_url=reverse_lazy("account:password_reset_complete"),
		template_name="account/password_reset_form.html"), name="password_reset_confirm"),
	
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
		template_name="account/password_reset_done.html"), name="password_reset_complete"),
]
