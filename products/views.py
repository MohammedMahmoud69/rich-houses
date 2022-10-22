from ast import keyword
from typing import Generic
from django.shortcuts import render
from .models import Product , Categories
from django.views.generic import ListView
# Create your views here.

# producte list view
def producte_list(request):
    product_list = Product.objects.all().order_by('-date')

    return render(request , 'products/product_list.html' , context={'products':product_list})

# product search view
def product_search(request):
    keyword = request.GET.get("search") 
    product_search = Product.objects.filter(name__icontains=keyword).order_by('-date')
    return render(request, 'products/product_search.html', context={'product_search':product_search})

# producte detail view
def producte_detail(request , slug):
    producte_detail = Product.objects.get(slug=slug)

    return render(request , 'products/product_detail.html' , context={'product':producte_detail})




