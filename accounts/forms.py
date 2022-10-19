from dataclasses import fields
from logging import PlaceHolder
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from captcha.fields import ReCaptchaField

class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email',]



    def __init__(self, *args, **kwargs): 
        super(UserForm, self).__init__(*args, **kwargs)                       
        self.fields['username'].disabled = True


class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['Full_Name' , 'Phone_Number' , 'Date',]



    def __init__(self, *args, **kwargs): 
        super(ProfileForm, self).__init__(*args, **kwargs)                       
        self.fields['Date'].disabled = True