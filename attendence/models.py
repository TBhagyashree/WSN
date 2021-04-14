from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class attendence(models.Model):
	Today_date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,to_field="username")
	Time_of_arrival = models.TimeField(auto_now_add=True)
	div=models.CharField(max_length=100)
	month = models.CharField(max_length=5,null=True)
	day =models.CharField(max_length=10,null=True)

	def __str__(self):
		t=str(self.user)
		return t


