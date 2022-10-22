from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product
from cart.cart import Cart
from .models import Order
from django.contrib.auth.decorators import login_required

# clear item function
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("order:order")

# increment item function
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("order:order")

# decrement item function
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("order:order")



# order furnction
@login_required(login_url='/accounts/login/')
def order(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        address = request.POST.get('address')
        zip = request.POST.get('zip')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)



        for one_product in cart:
            order = Order(
                user = user,
                product = cart[one_product]['name'],
                quantity = cart[one_product]['quantity'],
                price = cart[one_product]['price'],
                image = cart[one_product]['image'],
                city = city,
                address = address,
                zip = zip,
            )

            order.save()
            return redirect('orders:user_orders')
    
    return render(request , 'orders/checkout.html' , context={})

# user orders page function
@login_required(login_url='/accounts/login/')
def user_oredrs(request):
    user_orders = Order.objects.filter(user=request.user)

    return render(request,'orders/user_orders.html',context={'user_order':user_orders})