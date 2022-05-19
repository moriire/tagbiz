from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from datetime import datetime as dt

datenow = dt.now().year

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs = {"id": "email", "placeholder": "Email"}))
    password = forms.CharField(label='Password', max_length=12, widget=forms.PasswordInput(
        attrs = {"id": "password", "placeholder": "password"}
        ))

class RegistrationForm(forms.Form):
    phone = forms.IntegerField(label="Phone Number", widget=forms.TextInput(attrs={"class":"form-control-input", "placeholder":"+2348100482341", "id":"phone"}))
   
    first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput(attrs={"placeholder":"First Name", "id":"first-name"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"placeholder":"Last Name", "id":"last-name"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"id":"email", "placeholder":"Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"id":"password1", "placeholder":"Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"id":"password2", "placeholder":"Verify Password"}))

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            print(f"Password {password1} and {password2} doesnt match")
        else:
            return password2

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        userdata = CustomUser.objects.filter(phone=phone).first()#User.objects.filter(username)
        if not userdata:
            return phone
        else:
            print(f"username not in database")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        useremail = CustomUser.objects.filter(email=email).first()
        if not useremail:
            return email
        else:
            print(f"email not in database")

    def save(self, commit=True):
        users = CustomUser.objects.create_user(
            gender = self.cleaned_data.get("gender"),
            phone = self.cleaned_data.get("phone"),
            first_name = self.cleaned_data.get("first_name"),
            last_name = self.cleaned_data.get("last_name"),
            email = self.cleaned_data.get("email"),
            password = self.cleaned_data.get("password1"),)
        return users




