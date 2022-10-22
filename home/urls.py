from django.urls import path , include
from . import views

app_name = 'home'

urlpatterns = [
    # home page url
    path('', views.home , name='home'),
]
