from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .form import SignUpForm,EditProfileForm
from .models import Profile
# Create your views here.

def signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid : 
            form.save()
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('accounts:profile')
    else:
        form=SignUpForm()
        return render(request,'registration/signup.html',{'form':form,"title":"Sign Up"})
    

def profile(request):
    profile=get_object_or_404(Profile,user=request.user)
    return render(request,'accounts/profile.html',{"profile":profile})

@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile,user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            print(' done save  ')
            return redirect('accounts:profile')
    else:
        form = EditProfileForm(instance=profile)
    return render(request,"accounts/profile_edit.html",{'form':form,'pic':profile.image,'title':'Edit Profile'})


def candidates(request):
    pass
    
    