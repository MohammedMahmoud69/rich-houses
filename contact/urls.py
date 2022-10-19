from django.urls import path , include
from . import views
from . import api

app_name = 'contact'

urlpatterns = [
    path('' , views.contact , name='contact'),
    # messages api urls
    path('api/' , api.Message_List_Api.as_view() , name='Message_List_Api'),
    path('api/<int:id>/' , api.Message_Detail_Api.as_view() , name='Message_Detail_Api'),
]