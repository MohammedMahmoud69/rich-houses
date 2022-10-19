from django.urls import path , include
from . import views
from . import api

app_name = 'accounts'

urlpatterns = [
    # signup url
    path('signup/', views.register , name='signup'),
    # profile urls
    path('profile/', views.profile , name='profile'),
    path('profile/edit/', views.profile_edit , name='profile_edit'),
    # profile api urls
    path('api/profile/', api.Profile_List_Api.as_view() , name='profile_api'),
    path('api/profile/<int:id>/', api.Profile_Detail_Api.as_view() , name='profile_detail_api'),
    # user api urls
    path('api/user/', api.User_List_Api.as_view() , name='user_api'),
    path('api/user/<int:id>', api.User_Detail_Api.as_view() , name='user_detail_api'),
]