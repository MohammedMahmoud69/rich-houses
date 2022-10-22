from itertools import product
from django.shortcuts import render
from products.models import Product

# home function for home page

def home(request):
    products_by_price = Product.objects.all().order_by('price')[:10]
    products_by_date = Product.objects.all().order_by('-date')[:10]
    
    return render(request , 'home/index.html' , context={'products_by_price':products_by_price, 'products_by_date':products_by_date})


# 404 handle function
def page_404(request, exception):
    return render(request, 'home/404.html')