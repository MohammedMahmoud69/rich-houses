from django.shortcuts import render , redirect
from .models import Profile
from .forms import SignupForm , ProfileForm , UserForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
# Create your views here.



# register view

def register(request):
    if request.method == 'POST': 
        user_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():  
            user_save = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user_save
            profile.save()
            new_user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1'],
                )
            login(request, new_user)
            return redirect('accounts:profile')
         

    else:
        user_form = SignupForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form, 'profile_form': profile_form})


# profile view

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request , 'accounts/profile.html' , context={'profile':profile})




# profile edit view

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':

        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )

        if profileform.is_valid() and userform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('accounts:profile')

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})
