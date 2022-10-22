from django.urls import path
from . import views
from . import api

app_name = 'orders'

urlpatterns = [
     # order page url
     path('', views.order , name='order'),
     # user orders page url
     path('user_orders/', views.user_oredrs , name='user_orders'),
     # clear item url
     path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
     # item increment url
     path('item_increment/<int:id>/',views.item_increment, name='item_increment'),
     # item decrement url
     path('item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
     # order list api url
     path('api/', api.Order_List_Api.as_view() , name='order_list_api'),
     # order detail api url
     path('api/<int:id>/', api.Order_Detail_Api.as_view() , name='order_detail_api'),
]