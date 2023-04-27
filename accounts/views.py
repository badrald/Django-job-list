from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .form import SignUpForm,EditProfileForm,EditUserForm,CompanyForm
from .models import Profile,Company
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
    
@login_required
def profile(request):
    profile=get_object_or_404(Profile,user=request.user)
    return render(request,'accounts/profile.html',{"profile":profile})

@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile,user=request.user)
    if request.method == 'POST':
        formProfile = EditProfileForm(request.POST,request.FILES ,instance=profile)
        formUser=EditUserForm(request.POST,instance=profile.user)
        if formUser.is_valid() and formProfile.is_valid():
            formUser.save()
            myprofile = formProfile.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect('accounts:profile')
    else:
        formProfile = EditProfileForm(instance=profile)
        formUser=EditUserForm(instance=profile.user)
        return render(request,"accounts/profile_edit.html",{'form1':formUser,'form2':formProfile,'pic':profile.image,'title':'Edit Profile'})

@login_required
def create_company(request,profile_id):
    if request.method == "POST":
        form=CompanyForm(request.POST,request.FILES)
        if form.is_valid :
            form=form.save(commit=False)
            form.user=request.user
            form.profile=Profile.objects.get(id=profile_id)
            form.save()
            redirect('accounts:company',company.id)
    else:
        form=CompanyForm()
        return render(request,'accounts/company_profile.html',{'form':form,'tittle':"Company Profile"})

def candidates(request):
    profiles=Profile.objects.all()
    return render(request,'accounts/candidates.html',{"profiles":profiles})

def candidate(requets,id):
    profile=get_object_or_404(Profile,id=id)
    return render(requets,"accounts/candidate.html",{'profile':profile})

def companies(request):
    companies=Company.objects.all()
    return render(request,'accounts/companies.html',{"companies":companies})


def company(request,id):
    compnay=get_object_or_404(Company,id=id)
    return render(request,'accounts/company.html',{"company":compnay})

    
    