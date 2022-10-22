from django.urls import path
from . import views
from . import api 

app_name = 'about_us'

urlpatterns = [
    # about us url
    path('', views.about_us , name='about_us'),
    # about us api url
    path('api', api.about_api , name='about_api'),
]
