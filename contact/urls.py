from django.urls import path , include
from . import views
from . import api

app_name = 'contact'

urlpatterns = [
    # message page url
    path('' , views.contact , name='contact'),
    # message list api url
    path('api/' , api.Message_List_Api.as_view() , name='Message_List_Api'),
    # message detail api url
    path('api/<int:id>/' , api.Message_Detail_Api.as_view() , name='Message_Detail_Api'),
]