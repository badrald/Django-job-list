from django.shortcuts import render
from job.models import Job,Category
from accounts.models import Profile,Company
# Create your views here.

def index(request):
    jobs=Job.objects.all()[:6]
    categories=Category.objects.all()
    profiles=Profile.objects.all()[:6]
    companies=Company.objects.all()[:6]
    context={'Job':jobs,"Categories":categories,'profiles':profiles,'companies':companies}

    return render(request,'index.html',context)