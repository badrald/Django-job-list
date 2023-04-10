from django.shortcuts import render,get_object_or_404
from .models import Job,Category
from django.core.paginator import Paginator
# Create your views here.

def job_list(request):
    jobs=Job.objects.all()
    categories=Category.objects.all()
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'Jobs':page_obj,"Categories":categories , "count":jobs.count()}

    return render(request,'jobs.html',context)

def job_detail(request,slug):
    job=get_object_or_404(Job,slug=slug)
    context={'job':job}
    return render(request,'job_details.html',context)