from django.shortcuts import render , redirect
from .forms import Message_Form
# Create your views here.


# contact form view
def contact(request):
    
    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            form.save()
            form = Message_Form()
            return redirect('products:products')
    else:
        form = Message_Form()
        

    return render(request , 'contact/contact.html' , context={'form':form})

