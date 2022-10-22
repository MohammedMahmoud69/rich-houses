from django.urls import path
from . import views
from . import api


app_name = 'blog'

urlpatterns = [
    # blog list url
    path('' , views.blog_list , name='blogs'),
    # blog detail url
    path('search/' , views.blog_search , name='blog_search'),
    # blog list api url
    path('api/' , api.Blog_List_Api.as_view() , name='Blog_List_Api'),
    # blog detail api url
    path('api/<int:id>/' , api.Blog_Detail_Api.as_view() , name='Blog_Detail_Api'),
]

