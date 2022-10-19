from django.shortcuts import render, redirect
from products.models import Product
from cart.cart import Cart


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('products:products')

def cart_add_detail(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart:cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart:cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart:cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")



def cart_detail(request):
    return render(request, 'cart_app/cart.html')