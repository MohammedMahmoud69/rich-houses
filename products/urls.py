from django.urls import path
from . import views
from . import api

app_name = 'products'

urlpatterns = [
    # product list api url
    path('api/', api.Product_List_Api.as_view() , name='product_list_api'),

    # product detail api url
    path('api/<str:slug>/', api.Product_Detail_Api.as_view() , name='product_detail_api'),

    # product list url
    path('', views.producte_list , name='products'),

    # product search url
    path('search/', views.product_search , name='product_search'),
    
    # product detail url
    path('<str:slug>/', views.producte_detail , name='product'),
]