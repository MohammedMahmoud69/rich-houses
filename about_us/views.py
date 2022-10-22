from django.shortcuts import render
from .models import AboutUs

# about us view

def about_us(request):
    about_us = AboutUs.objects.all() # return all

    return render(request , 'about_us/about_us.html' , context={'about_us':about_us})