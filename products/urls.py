from django.urls import path
from . import views
from . import api

app_name = 'products'

urlpatterns = [
    # product api urls
    path('api/', api.Product_List_Api.as_view() , name='product_list_api'),
    path('api/<str:slug>/', api.Product_Detail_Api.as_view() , name='product_detail_api'),

    # product urls
    path('', views.producte_list , name='products'),
    path('search/', views.product_search , name='product_search'),
    path('<str:slug>/', views.producte_detail , name='product'),
]