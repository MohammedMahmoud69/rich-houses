from django.urls import path
from . import views
from . import api

app_name = 'orders'

urlpatterns = [
    # order urls
    path('', views.order , name='order'),
    path('user_orders/', views.user_oredrs , name='user_orders'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
     # order api urls
     path('api/', api.Order_List_Api.as_view() , name='order_list_api'),
     path('api/<int:id>/', api.Order_Detail_Api.as_view() , name='order_detail_api'),
]