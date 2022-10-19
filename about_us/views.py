from django.shortcuts import render
from .models import AboutUs
# Create your views here.

def about_us(request):
    about_us = AboutUs.objects.all()

    return render(request , 'about_us/about_us.html' , context={'about_us':about_us})