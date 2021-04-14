from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpadateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from .models import Profile


# Create your views here.

#function for signup
'''def signup_view(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('')

	else:
		form = UserCreationForm()

	return render(request, 'Authentication/signup_view.html',{'form':form})'''
token_generator=PasswordResetTokenGenerator()
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            
            message = render_to_string('Authenticate/acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token_generator.make_token(user),
            })
            token_generate=token_generator.make_token(user)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.add_message(request, messages.SUCCESS, 'Activate Your Account through Email.')
            return redirect('Authenticate:register')
    else:
        form = UserRegisterForm()
    return render(request, 'Authenticate/register.html', {'form': form})




def activate(request, uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        save_profile=Profile()
        save_profile.user=user
        save_profile.save()
        
        # return redirect('home')
        messages.add_message(request, messages.SUCCESS, 'Account Activated, Login.')
        return redirect('Authenticate:login')
    else:
        return HttpResponse('Activation link is invalid!')








'''def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created for {username}! You are now able to login')
            

    else:
        form = UserRegisterForm()
    return render(request,'Authenticate/register.html',{'form':form})'''

@login_required
def Settings(request):
    if request.method == 'POST':
        u_form = UserUpadateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username}, Your account has been updated!')
            return redirect('Authenticate:Settings')
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'Authenticate/settings_teacher.html',context)



@login_required
def Settings_student(request):
    if request.method == 'POST':
        u_form = UserUpadateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username}, Your acoount has been updated!')
            return redirect('Authenticate:Settings_student')
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'Authenticate/settings_student.html',context)

#function for login
def login_view(request):
    if request.method=='POST':
        print(request.POST['username'])
        form = authenticate(username=request.POST['username'],password=request.POST['pass'])
        try:
            if form.is_active:
                if form.is_superuser:
                    user1 = form
                    login(request,user1)
                    return redirect('Teacher:Teacher_view_dashboard')
                else:
                    user2 = form
                    login(request,user2)
                    return redirect('attendence:attendence_student')
        except:
            messages.add_message(request, messages.WARNING, 'Incorrect credentials, Try again.')
            return render(request, 'Authenticate/login_view.html')
    return render(request, 'Authenticate/login_view.html')



#function for logout
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('Authenticate:login')
    logout(request)
    return redirect('Authenticate:login')

@login_required
def profile_teacher(request):
    return render(request, 'Authenticate/profile_teacher.html')


def profile_student(request):
    return render(request,'Authenticate/profile_student.html')
