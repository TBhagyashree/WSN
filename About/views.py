from django.shortcuts import render

# Create your views here.
def About_view_student(request):
	return render(request,'About/About_base_student.html')

def About_view_teacher(request):
	return render(request,'About/About_base_teacher.html')