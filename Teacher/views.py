from django.shortcuts import render,redirect,HttpResponse
from .models import division,Timetable
from student.models import Student_detail
from datetime import datetime
from attendence.models import attendence
import calendar
from datetime import datetime,time,timedelta
# Create your views here.
import pandas as pd
import csv
import pdfkit as pdf
import convertapi

from django.contrib import messages
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from googleapiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode
from google_auth_oauthlib.flow import InstalledAppFlow
import urllib, mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import os
import base64
from selenium import webdriver



set_div=[]





def Teacher_view(request):
	return render(request, 'Teacher/Teacher_view.html')

def Time_table(request):
	if request.method=='POST':
		starttime=request.POST['start']
		endtime=request.POST['end']
		lec=request.POST['lec']
		Day=request.POST['Day']
		type_of_lec=request.POST['type']

		time=Timetable()
		time.start_time=starttime
		time.end_time=endtime
		time.day=Day
		time.Lec=lec
		if type_of_lec=="Lab":
			batch=request.POST['batch']
			time.Batch=batch
		time.type_of=type_of_lec
		try:
			time.division=set_div[0]
			time.save()
		except:
			messages.add_message(request, messages.WARNING, 'Division Not Selected.')

		
	try:
		'''name=""
		monday_lab_dict={}
		monday_lec=Timetable.objects.all().filter(day="Monday").filter(division=set_div[0],type_of="Lec").order_by('start_time')
		monday_lab=Timetable.objects.all().filter(day="Monday").filter(division=set_div[0],type_of="Lab").order_by('start_time')
		for i in monday_lab:
			name=i
			starttime=i.start_time
			for j in monday_lab:
				if i.Lec==j.Lec:
					None
				else:
					if i.start_time==j.start_time:
						name+=j
					else:
						None
			monday_lab_dict.update({"start_time":starttime,"Lec":name})'''
			
		monday=Timetable.objects.all().filter(day="Monday").filter(division=set_div[0]).order_by('start_time')

	except:
		monday=None

	try:
		tuesday=Timetable.objects.all().filter(day="Tuesday").filter(division=set_div[0]).order_by('start_time')
	except:
		tuesday=None

	try:
		wednesday=Timetable.objects.all().filter(day="Wednesday").filter(division=set_div[0]).order_by('start_time')
	except:
		wednesday=None

	try:
		thursday=Timetable.objects.all().filter(day="Thursday").filter(division=set_div[0]).order_by('start_time')
	except:
		thursday=None

	try:
		friday=Timetable.objects.all().filter(day="Friday").filter(division=set_div[0]).order_by('start_time')
	except:
		friday=None

	try:
		saturday=Timetable.objects.all().filter(day="Saturday").filter(division=set_div[0]).order_by('start_time')
	except:
		saturday=None

	try:
		give_div=set_div[0]
	except:
		give_div=None

	return render(request, 'Teacher/Time_table.html',{"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday,"saturday":saturday,"division":give_div})

def Teacher_view_dashboard(request):
	
	if request.method=='POST':
		div= division.objects.all()
		if len(request.POST['division'])!=0:
			set_div1=request.POST['division']
			if len(set_div)!=0:
				set_div.pop(0)
			set_div.append(set_div1)

	if len(set_div)!=0:
		div= division.objects.all()
		try:
			
			check_div=set_div[0]
			monday=Timetable.objects.all().filter(division=check_div,day="Monday").order_by('start_time')
			tuesday=Timetable.objects.all().filter(division=check_div,day="Tuesday").order_by('start_time')
			wednesday=Timetable.objects.all().filter(division=check_div,day="Wednesday").order_by('start_time')
			thursday=Timetable.objects.all().filter(division=check_div,day="Thursday").order_by('start_time')
			friday=Timetable.objects.all().filter(division=check_div,day="Friday").order_by('start_time')
			saturday=Timetable.objects.all().filter(division=check_div,day="Saturday").order_by('start_time')
			return render(request, 'Teacher/Teacher_view_dashboard.html',{"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday,"saturday":saturday,'div':div,'div1':set_div[0]})
		except:
			div= division.objects.all()
			return render(request, 'Teacher/Teacher_view_dashboard.html',{'div':div})
	else:
		div= division.objects.all()
		return render(request, 'Teacher/Teacher_view_dashboard.html',{'div':div})




def students(request):
	try:
		student=Student_detail.objects.all().filter(Student_division=set_div[0])
	except:
		student=None

	return render(request, 'Teacher/students.html',{'students':student})



def email(request):
	if request.method=='POST':
		try:
			to=request.POST['to']
			subject=request.POST['subject']
			From=str(request.user)
			f=str(request.FILES['file'])
			try:
				cc=request.POST['cc']
			except:
				cc=""

			content=request.POST['body']
			
			SCOPE = 'https://www.googleapis.com/auth/gmail.compose'
			#store = file.Storage('credentials.json')
			creds = None
			if not creds or creds.invalid:
				flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPE)

				try:
					creds = flow.run_local_server(port=8080,open_browser=True)
					
				except:
					creds = flow.run_local_server(port=4545,open_browser=True)
					
			service = build('gmail', 'v1',credentials=creds)


			def create_message_with_attachment(sender, to, cc,subject, message_text, file):
				msg = MIMEMultipart()
				msg['From'] = sender
				msg['To'] = to
				msg['cc']=cc
				msg['Subject'] = subject

				fp = open(f, 'rb')
				attach = MIMEApplication(fp.read(), 'pdf')
				fp.close()
				attach.add_header('Content-Disposition', 'attachment', filename = 'file.pdf')
				msg.attach(attach)
				raw_message = base64.urlsafe_b64encode(msg.as_string().encode("utf-8"))
				return {'raw': raw_message.decode("utf-8")}


			# https://developers.google.com/gmail/api/guides/sending
			def send_message(service, user_id, message):
			  """Send an email message.
			  Args:
			    service: Authorized Gmail API service instance.
			    user_id: User's email address. The special value "me"
			    can be used to indicate the authenticated user.
			    message: Message to be sent.
			  Returns:
			    Sent Message.
			  """
			  try:
			    message = (service.users().messages().send(userId=user_id, body=message)
			               .execute())
			    
			    messages.add_message(request, messages.SUCCESS, 'Email Sent.')
			    return message
			  #except errors.HttpError, error:
			  except:
			    print('An error occurred: %s' % error)


			raw_msg = create_message_with_attachment(From, to,cc, subject, content,f)
			send_message(service, "me", raw_msg)
		except:
			messages.add_message(request, messages.WARNING, 'Email Was Not Sent.')
		
	return render(request, 'Teacher/email.html')


def Time_table_delete(request):
	if request.method=="POST":
		start=request.POST['start']
		end=request.POST['end']
		lec=request.POST['lec']
		Day=request.POST['day']
		type_of_lec=request.POST['type_of']
		print(start,end,lec,Day,type_of_lec)
		
		div=set_div[0]

		dele=Timetable.objects.all().filter(division=div,start_time=start,end_time=end,Lec=lec,day=Day,type_of=type_of_lec)
		dele.delete()


		return redirect('Teacher:Time_table')
	return redirect('Teacher:Time_table')


def weekday_count(start, end):
  start_date  = datetime.strptime(start, '%d/%m/%Y')
  end_date    = datetime.strptime(end, '%d/%m/%Y')
  week        = {}
  for i in range((end_date - start_date).days):
    day       = calendar.day_name[(start_date + timedelta(days=i+1)).weekday()]
    week[day] = week[day] + 1 if day in week else 1
  return week






def Calculate_attendence(request):
	try:
		students=Student_detail.objects.all().filter(Student_division=set_div[0])
		lecs=Timetable.objects.all().filter(division=set_div[0],type_of="Lec")
		labs=Timetable.objects.all().filter(division=set_div[0],type_of="Lab")
		



		make_list_lec=[]
		make_list_lab=[]

		# list of lec and lab
		for lec in lecs:
			if lec.Lec in make_list_lec:
				None
			else:
				make_list_lec.append(lec.Lec)


		for lab in labs:
			if lab.Lec in make_list_lab:
				continue
			else:
				make_list_lab.append(lab.Lec)

		today = datetime.today()
		datem=int(today.strftime("%d"))
		monthm = today.strftime("%m")
		monthm1=int(today.strftime("%m"))
		yearm = int(today.strftime("%Y"))
		start=('1/'+str(monthm1)+'/'+str(yearm))
		end=(str(datem)+'/'+str(monthm1)+'/'+str(yearm))	
		get=weekday_count(str(start),str(end))

		total_lec_dict={}
		total_lab_dict_final={}
		for a in lecs:
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
		batch=[]
		for b in labs:
			if b.Batch in batch:
				None
			else:
				batch.append(b.Batch)
				batch.sort()
		

		for ba in batch:
			labs1=Timetable.objects.all().filter(division=set_div[0],type_of="Lab",Batch=ba)
			total_lab_dict={}
			for a in labs1:
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
			total_lab_dict_final.update({ba:total_lab_dict})

		
		
		overall={}
		for student in students:
			attendence_student=attendence.objects.all().filter(div=set_div[0],month=monthm,user=student.user)
			dict_lec={}
			dict_lab={}
			for attend_lec in attendence_student:
				
				for lec in lecs:
					if lec.start_time<attend_lec.Time_of_arrival and lec.end_time>attend_lec.Time_of_arrival and lec.day==attend_lec.day :
						if lec.Lec in dict_lec:
							value=dict_lec[lec.Lec]
							dict_lec[lec.Lec]=value+1
						else:
							dict_lec.update({lec.Lec:1})
					else:
						if lec.Lec in dict_lec:
							None
						else:
							dict_lec.update({lec.Lec:0})

				for lab in labs:
					if lab.start_time<attend_lec.Time_of_arrival and lab.end_time>attend_lec.Time_of_arrival and lab.day==attend_lec.day and student.Batch==lab.Batch:
						if lab.Lec in dict_lab:
							value=dict_lab[lab.Lec]
							dict_lab[lab.Lec]=value+1
						else:
							dict_lab.update({lab.Lec:1})
					else:
						if lab.Lec in dict_lab:
							None
						else:
							dict_lab.update({lab.Lec:0})

			if len(dict_lec)==0 and len(dict_lab)==0:
				messages.add_message(request, messages.WARNING, 'No attendance for this month.')
			return render(request,"Teacher/attendence.html")


			percent_lec_dict={}
			percent_lab_dict={}

			for f in make_list_lec:

				percent_lec=round((dict_lec[f]/total_lec_dict[f])*100)
				percent_lec_dict.update({f:percent_lec})
			
			for ff in make_list_lab:
				
				percent_lab=round((dict_lab[ff]/total_lab_dict_final[student.Batch][ff])*100)
				percent_lab_dict.update({ff:percent_lab})

			total_percent=round(((sum(dict_lec.values())+sum(dict_lab.values()))/(sum(total_lec_dict.values())+sum(total_lab_dict_final[student.Batch].values())))*100,2)


			overall.update({student:{"lec_percent":percent_lec_dict,"lab_percent":percent_lab_dict,"total_percent":total_percent}})
		total_students=len(overall.keys())


		crictical_defaulter=0
		defaulter=0

		for student1 in overall:
			
			total= overall[student1]["total_percent"]
			
			if total < 65.00 :
				crictical_defaulter+=1

			if total < 75.00:
				defaulter+=1
		
		if request.method=="POST":
			with open("report.csv",'w') as file:
				row_list=[]
				writer = csv.writer(file)
				head=["student"]
				for i in make_list_lec:
					head.append(i+" Lec")
					


				for j in make_list_lab:
					head.append(j+" Lab")
				head.append("Total")
				row_list.append(head)
				for student in overall:
					data=[]
					student_name=student.Student_first_name+" "+student.Student_last_name
					data.append(student_name)
					for i in make_list_lec:
						data.append(overall[student]["lec_percent"][i])
					for j in make_list_lab:
						data.append(overall[student]["lab_percent"][j])

					data.append(overall[student]["total_percent"])

					row_list.append(data)




				

				writer.writerows(row_list)

			csv_file = 'report.csv'
			html_file = csv_file[:-3]+'html'
			pdf_file = csv_file[:-3]+'pdf'
			df = pd.read_csv(csv_file, sep=',')
			df.to_html(html_file)
			convertapi.api_secret = 'dQY9CDzsUFlRWHNb'
			convertapi.convert('pdf', {
			    'File': 'report.html'
			}, from_format = 'html').save_files(pdf_file)
			







		return render(request,"Teacher/attendence.html",{"overall":overall,"total_lec_dict":total_lec_dict,"total_lab_dict":total_lab_dict_final,"list_lec":make_list_lec,"list_lab":make_list_lab,"total_students":total_students,"batch":batch,"critical":crictical_defaulter,"defaulter":defaulter})
	except:
		messages.add_message(request, messages.WARNING, 'Check Division.')
		return render(request,"Teacher/attendence.html")

