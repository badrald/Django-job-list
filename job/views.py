from django.shortcuts import render,get_object_or_404
from .models import Job,Category
# Create your views here.

def job_list(request):
    jobs=Job.objects.all()
    categories=Category.objects.all()
    
    context={'Job':jobs,"Categories":categories}

    return render(request,'jobs.html',context)

def job_detail(request,id):
    job=get_object_or_404(Job,id=id)
    context={'job':job}
    return render(request,'job_details.html',context)