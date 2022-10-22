from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

# User form for sign up
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
# User form for profile edit
class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

    # function for disabled username field
    def __init__(self, *args, **kwargs): 
        super(UserForm, self).__init__(*args, **kwargs)                       
        self.fields['username'].disabled = True


# profile form
class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['Full_Name' , 'Phone_Number' , 'Date',]

    # function for disabled date field
    def __init__(self, *args, **kwargs): 
        super(ProfileForm, self).__init__(*args, **kwargs)                       
        self.fields['Date'].disabled = True