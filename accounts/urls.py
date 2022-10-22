from django.urls import path , include
from . import views
from . import api

app_name = 'accounts'

urlpatterns = [
    # signup url
    path('signup/', views.register , name='signup'),
    # profile url
    path('profile/', views.profile , name='profile'),
    # profile edit url
    path('profile/edit/', views.profile_edit , name='profile_edit'),
    # profile list api url
    path('api/profile/', api.Profile_List_Api.as_view() , name='profile_api'),
    # profile detail api url
    path('api/profile/<int:id>/', api.Profile_Detail_Api.as_view() , name='profile_detail_api'),
    # user list api url
    path('api/user/', api.User_List_Api.as_view() , name='user_api'),
    # user detail api url
    path('api/user/<int:id>', api.User_Detail_Api.as_view() , name='user_detail_api'),
]