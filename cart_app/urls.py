from django.urls import path
from . import views

app_name = 'cart_app'

# cart actions urls
urlpatterns = [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('add_list/<int:id>/', views.cart_add_detail, name='cart_add_detail'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
]