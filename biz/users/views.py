#from . import token
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from . registration import RegistrationForm, LoginForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import  (PasswordResetView, PasswordResetConfirmView, PasswordChangeView)
from django.contrib.auth import forms, views
from django.urls import reverse_lazy
from .forms import UserPasswordResetForm

class PasswordReset(views.PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    extra_email_context = None
    #form_class = UserPasswordResetForm
    from_email = "admin@fikifaka.com"
    html_email_template_name = None
    #subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'

def signout(request):
    logout(request)
    return redirect("/")#render(request, "./registration/logout.html", dict(form='logged-out'))

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/loggedin')
    next = request.POST.get("next")
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if next=="":
                    return redirect("/")

                elif next is not None:
                    return redirect(next)
                #redirect("/loggedin")
            else:
                messages.error(request, 'User not found')
        else:
            messages.error(request, "Invalid login credentials. Pls use the register button")
            #return redirect('/auth/login')
    return render(request, "registration/login.html", dict(form=form))

def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #gender = request.POST["gender"]
            #phone = request.POST["phone"]
            #password = request.POST["password1"]
            if form.is_valid():
                form.save()
                #new_login=authenticate(username=username, password=password)
                #login(User, new_login)
                return redirect("/")
            else:
                messages.success(request, "Reg successful!")
                return redirect('login/')
        else:
            messages.error(request, form.errors)

    else:
        form=RegistrationForm()
    return render(request, "./registration/register.html", dict(form=form))

def loggedin(request):
    return redirect(request, "registration/loggedin")
