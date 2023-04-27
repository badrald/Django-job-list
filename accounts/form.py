from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Profile ,Company


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'email',"password1","password2",)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = '__all__'
        exclude= ('user',)

class EditUserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username','email','first_name','last_name']

class CompanyForm(forms.ModelForm):
    class Meta:
        model= Company
        fields ='__all__'
        exclude = ('profile','user')
