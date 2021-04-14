from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student_detail(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,to_field="username")


	Student_first_name=models.CharField(max_length=100,null=True)
	Student_middle_name=models.CharField(max_length=100,null=True)
	Student_last_name=models.CharField(max_length=100,null=True)
	Student_gender=models.CharField(max_length=100,null=True)
	Student_email=models.EmailField(max_length=100,null=True)
	Student_dob=models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
	Student_division=models.CharField(max_length=50,null=True)
	Student_card=models.CharField(max_length=50,blank=True,null=True)
	Batch=models.CharField(max_length=10,null=True)


	Parent_first_name=models.CharField(max_length=100,null=True)
	Parent_middle_name=models.CharField(max_length=100,null=True)
	Parent_last_name=models.CharField(max_length=100,null=True)
	Parent_email=models.EmailField(max_length=100,blank=True,null=True)
	Parent_phone=models.IntegerField(blank=True,null=True)



	def __str__(self):
		return self.Student_first_name