from django.shortcuts import render,HttpResponse
from student.models import Student_detail
from Teacher.models import division,Timetable
from datetime import datetime,time,timedelta
import calendar
import pytz
from .models import attendence
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def weekday_count(start, end):
  start_date  = datetime.strptime(start, '%d/%m/%Y')
  end_date    = datetime.strptime(end, '%d/%m/%Y')
  week        = {}
  for i in range((end_date - start_date).days):
    day       = calendar.day_name[(start_date + timedelta(days=i+1)).weekday()]
    week[day] = week[day] + 1 if day in week else 1
  return week



def attendence_student(request):
	today = datetime.today()
	datem = today.strftime("%m")
	try:
		check_attendence=attendence.objects.all().filter(month=datem,user=request.user)
		get_div=Student_detail.objects.get(user=request.user)
		check_division=get_div.Student_division
		check_batch=get_div.Batch
		
		check_lec=Timetable.objects.all().filter(type_of="Lec",division=check_division)
		check_lab=Timetable.objects.all().filter(type_of="Lab",division=check_division,Batch=check_batch)
		list_lec=[]
		list_lab=[]

		dict_lec={}
		dict_lab={}
		checking_present= "no"

		# for lecs
		for lec in check_lec:
			if len(list_lec)!=0:

				for li in list_lec:
					if lec.Lec == li:
						checking_present="yes"
						break
					else:
						checking_present="no"
						pass
				if checking_present=="no":
					list_lec.append(lec.Lec)
					dict_lec.update({lec.Lec:0})
			else:
				list_lec.append(lec.Lec)
				dict_lec.update({lec.Lec:0})

		
		for i in check_attendence:
			get_time=str(i.Time_of_arrival.replace(microsecond=0))
			#time1=time(hour = 11, minute = 34, second = 56)
			time1=i.Time_of_arrival.replace(microsecond=0)
			for j in check_lec:
				
				if (time1 > j.start_time) and (time1 < j.end_time) and i.day==j.day:
					# something
					lec=j.Lec
					if lec in dict_lec:
						value=dict_lec[lec] 
						dict_lec[lec]=value+1
					else:
						dict_lec.update({lec:1})

					break

				else:
					pass
	

		#for lab
		for lab in check_lab:
			if len(list_lab)!=0:
				if lab.Lec in check_lab:
					continue
				else:
					list_lab.append(lab.Lec)
					dict_lab.update({lab.Lec:0})
			else:
				list_lab.append(lab.Lec)
				dict_lab.update({lab.Lec:0})

		


		for i in check_attendence:
			get_time=str(i.Time_of_arrival.replace(microsecond=0))
			#time1=time(hour = 11, minute = 34, second = 56)
			time1=i.Time_of_arrival.replace(microsecond=0)
			for j in check_lab:
				
				if (time1 > j.start_time) and (time1 < j.end_time) and i.day==j.day:
					# something
					lec=j.Lec
					if lec in dict_lab:
						value=dict_lab[lec] 
						dict_lab[lec]=value+1
					else:
						dict_lab.update({lec:1})

					break

				else:
					pass



		# count total no lecs for this month
		today = datetime.today()
		datem=int(today.strftime("%d"))
		monthm = int(today.strftime("%m"))
		yearm = int(today.strftime("%Y"))
		
		#get_current_date=calendar.monthrange(yearm,monthm)
		#get_day_end=get_current_date[1]
		start=('1/'+str(monthm)+'/'+str(yearm))
		end=(str(datem)+'/'+str(monthm)+'/'+str(yearm))
		
		get=weekday_count(str(start),str(end))
		
		total_lec_dict={}
		total_lab_dict={}
		for a in check_lec:
			lec=a.Lec
			day=a.day
			if lec in total_lec_dict:
				get_no_days=get[day]
				count=total_lec_dict[lec]
				count=count+get_no_days
				total_lec_dict[lec]=count

			else:
				get_no_days=get[day]
				total_lec_dict.update({lec:get_no_days})


		for a in check_lab:
			lec=a.Lec
			day=a.day
			if lec in total_lab_dict:
				get_no_days=get[day]
				count=total_lec_dict[lec]
				count=count+get_no_days
				total_lab_dict[lec]=count

			else:
				get_no_days=get[day]
				total_lab_dict.update({lec:get_no_days})
		


		# calculate percentage for lec
		percent_lec_dict={}
		percent_lab_dict={}
		for f in list_lec:

			percent_lec=round((dict_lec[f]/total_lec_dict[f])*100)
			percent_lec_dict.update({f:percent_lec})
		
		for ff in list_lab:
			percent_lab=round((dict_lab[ff]/total_lab_dict[ff])*100)
			percent_lab_dict.update({ff:percent_lab})

		


		total_percent=round(((sum(dict_lec.values())+sum(dict_lab.values()))/(sum(total_lec_dict.values())+sum(total_lab_dict.values())))*100,2)

		return render(request, "attendence/attendence_student.html",  {"list_lec":list_lec,"dict_lec":dict_lec,"total_lec_dict":total_lec_dict,"percent_lec_dict":percent_lec_dict,"list_lab":list_lab,"dict_lab":dict_lab,"total_lab_dict":total_lab_dict,"percent_lab_dict":percent_lab_dict,"total_percent":total_percent})

	except:
		return render(request, "attendence/attendence_student.html")

@csrf_exempt
# Create your views here.
def attendence_save(request):
	if request.method=='POST':
		card=request.POST['card']
		print(card)
		check_student=Student_detail.objects.get(Student_card=card)
		check_division=check_student.Student_division
		check_student_name=check_student.user


		get_div=division.objects.get(division=check_division)

		now=datetime.now()
		current_time=now.strftime("%H_%M")
		print(current_time)
		today = datetime.today()
		daym=today.strftime("%A")
		datem = today.strftime("%m")
		save_attendence=attendence()
		save_attendence.user=check_student_name
		save_attendence.div=check_division
		save_attendence.month=datem
		save_attendence.day=daym
		save_attendence.save()

	return None
		


def defaulters(request):
	return render(request,"attendence/defaulters.html")







