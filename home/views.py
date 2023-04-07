from django.shortcuts import render
from job.models import Job,Category
# Create your views here.

def index(request):
    jobs=Job.objects.all()[:6]
    categories=Category.objects.all()
    context={'Job':jobs,"Categories":categories}

    return render(request,'index.html',context)