from django import forms
from .models import Blog

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields= '__all__'
        exclude= ('profile','slug',)