from django import forms
from .models import Contact


class Message_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

