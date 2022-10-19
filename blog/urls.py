from django.urls import path
from . import views
from . import api


app_name = 'blog'

urlpatterns = [
    # blog urls
    path('' , views.blog_list , name='blogs'),
    path('search/' , views.blog_search , name='blog_search'),
    # blog api urls
    path('api/' , api.Blog_List_Api.as_view() , name='Blog_List_Api'),
    path('api/<int:id>/' , api.Blog_Detail_Api.as_view() , name='Blog_Detail_Api'),
]

