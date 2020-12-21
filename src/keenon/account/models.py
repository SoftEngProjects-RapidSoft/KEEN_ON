from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User,null=True, blank=True, on_delete= models.CASCADE)
	image = models.ImageField(default='defaultProfile.png',null=True, blank=True)
	phone =  models.CharField(max_length= 12, null=True)
	def _str_(self):
		return self.user.username

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
