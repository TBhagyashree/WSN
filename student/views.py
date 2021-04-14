from django.shortcuts import render
from .models import Student_detail
from django.contrib.auth.models import User
from Teacher.models import division,Timetable

# Create your views here.
def student_view(request):
	try:
		student=Student_detail.objects.get(user=request.user.username)
		student_convert=str(student)

	except:
		student_convert=''	

	print(student_convert)

	if(len(student_convert)!=0):
		info=Student_detail.objects.get(user=request.user.username)
		try:
			check=Student_detail.objects.get(user=request.user.username)
			check_div=check.Student_division



			monday=Timetable.objects.all().filter(division=check_div,day="Monday")
			tuesday=Timetable.objects.all().filter(division=check_div,day="Tuesday")
			wednesday=Timetable.objects.all().filter(division=check_div,day="Wednesday")
			thursday=Timetable.objects.all().filter(division=check_div,day="Thursday")
			friday=Timetable.objects.all().filter(division=check_div,day="Friday")
			saturday=Timetable.objects.all().filter(division=check_div,day="Saturday")

			return render(request, 'student/student_view.html',{'info':info,"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday,"saturday":saturday,"div":check_div})
		except:
			return render(request, 'student/student_view.html',{'info':info})

	else:
		try:
			check=Student_detail.objects.get(user=request.user.username)
			check_div=check.Student_division



			monday=Timetable.objects.all().filter(division=check_div,day="Monday")
			tuesday=Timetable.objects.all().filter(division=check_div,day="Tuesday")
			wednesday=Timetable.objects.all().filter(division=check_div,day="Wednesday")
			thursday=Timetable.objects.all().filter(division=check_div,day="Thursday")
			friday=Timetable.objects.all().filter(division=check_div,day="Friday")
			saturday=Timetable.objects.all().filter(division=check_div,day="Saturday")

			return render(request, 'student/student_view.html',{'info':info,"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday,"saturday":saturday,"div":check_div})
		except:
			return render(request, 'student/student_view.html')


def student_detail(request):
	print(request.user.username)
	if request.method=='POST':
		fname=request.POST['firstName']
		mname=request.POST['middleName']
		lname=request.POST['lastName']
		gender=request.POST['gender']
		email=request.POST['email']
		dob=request.POST['DOB']
		div=request.POST['division']
		pfname=request.POST['pFirstName']
		pmname=request.POST['pMiddleName']
		plname=request.POST['pLastName']
		phone=request.POST['Phone']
		pemail=request.POST['pEmail']
		card=request.POST['card']
		batch=request.POST['batch']
			
		try:
			student=Student_detail.objects.get(user=request.user.username)
			student_converted=str(student)

		except:
			student_converted=''


		if(len(student_converted)!=0):
			detail_save=Student_detail.objects.get(user=request.user.username)


			if len(fname)!=0:
				detail_save.Student_first_name=fname
			if len(mname)!=0:
				detail_save.Student_middle_name=mname
			if len(lname)!=0:
				detail_save.Student_last_name=lname
			if len(gender)!=0:
				detail_save.Student_gender=gender
			if len(email)!=0:
				detail_save.Student_email=email
			if len(dob)!=0:
				detail_save.Student_dob=dob
			if len(div)!=0:
				detail_save.Student_division=div
			if len(pfname)!=0:
				detail_save.Parent_first_name=pfname
			if len(pmname)!=0:
				detail_save.Parent_middle_name=pmname
			if len(plname)!=0:
				detail_save.Parent_last_name=plname
			if len(pemail)!=0:
				detail_save.Parent_email=pemail
			if len(phone)!=0:
				detail_save.Parent_phone=phone
			if len(card)!=0:
				detail_save.Student_card=card
			if len(batch)!=0:
				detail_save.Batch=batch

			detail_save.save()
		else:
			print('not available')
			user=User.objects.get(username=request.user.username)
			detail_save=Student_detail()
			detail_save.user=user
			if len(fname)!=0:
				detail_save.Student_first_name=fname
			if len(mname)!=0:
				detail_save.Student_middle_name=mname
			if len(lname)!=0:
				detail_save.Student_last_name=lname
			if len(gender)!=0:
				detail_save.Student_gender=gender
			if len(email)!=0:
				detail_save.Student_email=email
			if len(dob)!=0:
				detail_save.Student_dob=dob
			if len(div)!=0:
				detail_save.Student_division=div
			if len(pfname)!=0:
				detail_save.Parent_first_name=pfname
			if len(pmname)!=0:
				detail_save.Parent_middle_name=pmname
			if len(plname)!=0:
				detail_save.Parent_last_name=plname
			if len(pemail)!=0:
				detail_save.Parent_email=pemail
			if len(phone)!=0:
				detail_save.Parent_phone=phone
			if len(card)!=0:
				detail_save.Student_card=card
			if len(batch)!=0:
				detail_save.Batch=batch

			detail_save.save()
		

	try:
		student=Student_detail.objects.get(user=request.user.username)
		student_convert=str(student)

	except:
		student_convert=''	

	print(student_convert)
	if(len(student_convert)!=0):
		info=Student_detail.objects.get(user=request.user.username)
		return render(request, 'student/detail.html',{'info':info})
	else:
		return render(request, 'student/detail.html')


def timetable(request):
	try:
		check=Student_detail.objects.get(user=request.user.username)
		check_div=check.Student_division

		
		monday=Timetable.objects.all().filter(division=check_div,day="Monday").order_by("start_time")
		tuesday=Timetable.objects.all().filter(division=check_div,day="Tuesday").order_by("start_time")
		wednesday=Timetable.objects.all().filter(division=check_div,day="Wednesday").order_by("start_time")
		thursday=Timetable.objects.all().filter(division=check_div,day="Thursday").order_by("start_time")
		friday=Timetable.objects.all().filter(division=check_div,day="Friday").order_by("start_time")
		saturday=Timetable.objects.all().filter(division=check_div,day="Saturday").order_by("start_time")
		return render(request, 'student/timetable.html',{"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday,"saturday":saturday,"div":check_div})
	except:
		return render(request, 'student/timetable.html')
	