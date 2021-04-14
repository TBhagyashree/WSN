from django.db import models

# Create your models here.
class division(models.Model):
	division = models.CharField(max_length=10)
	lec1 = models.CharField(max_length=50,blank=True,default=None)
	lec2 = models.CharField(max_length=50,blank=True,default=None)
	lec3 = models.CharField(max_length=50,blank=True,default=None)
	lec4 = models.CharField(max_length=50,blank=True,default=None)
	lec5 = models.CharField(max_length=50,blank=True,default=None)
	lec6 = models.CharField(max_length=50,blank=True,default=None)
	lec7 = models.CharField(max_length=50,blank=True,default=None)
	lec8 = models.CharField(max_length=50,blank=True,default=None)
	lec9 = models.CharField(max_length=50,blank=True,default=None)
	lec10 = models.CharField(max_length=50,blank=True,default=None)
	lec11 = models.CharField(max_length=50,blank=True,default=None)
	lec12 = models.CharField(max_length=50,blank=True,default=None)
	lec13 = models.CharField(max_length=50,blank=True,default=None)
	lec14 = models.CharField(max_length=50,blank=True,default=None)
	lec15 = models.CharField(max_length=50,blank=True,default=None)
	lec16 = models.CharField(max_length=50,blank=True,default=None)
	lec17 = models.CharField(max_length=50,blank=True,default=None)
	lec18 = models.CharField(max_length=50,blank=True,default=None)
	lec19 = models.CharField(max_length=50,blank=True,default=None)
	lec20 = models.CharField(max_length=50,blank=True,default=None)
	lec21 = models.CharField(max_length=50,blank=True,default=None)
	lec22 = models.CharField(max_length=50,blank=True,default=None)
	lec23 = models.CharField(max_length=50,blank=True,default=None)
	lec24 = models.CharField(max_length=50,blank=True,default=None)
	lec25 = models.CharField(max_length=50,blank=True,default=None)
	lec26 = models.CharField(max_length=50,blank=True,default=None)
	lec27 = models.CharField(max_length=50,blank=True,default=None)
	lec28 = models.CharField(max_length=50,blank=True,default=None)
	lec29 = models.CharField(max_length=50,blank=True,default=None)
	lec30 = models.CharField(max_length=50,blank=True,default=None)
	lec31 = models.CharField(max_length=50,blank=True,default=None)
	lec32 = models.CharField(max_length=50,blank=True,default=None)
	lec33 = models.CharField(max_length=50,blank=True,default=None)
	lec34 = models.CharField(max_length=50,blank=True,default=None)
	lec35 = models.CharField(max_length=50,blank=True,default=None)
	lec36 = models.CharField(max_length=50,blank=True,default=None)



	def __str__(self):
		return self.division




class Timetable(models.Model):
	division=models.CharField(max_length=10)
	start_time=models.TimeField(blank=True)
	end_time=models.TimeField(blank=True)
	day=models.CharField(max_length=20)
	Lec=models.CharField(max_length=50)
	type_of=models.CharField(max_length=20)
	Batch=models.CharField(max_length=10,null=True)


	def __str__(self):
		return self.Lec