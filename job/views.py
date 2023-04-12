from django.shortcuts import render,get_object_or_404,redirect
from .models import Job,Category

from django.contrib.auth.decorators import login_required

from .form import ApplyForm,JobForm

from django.urls import reverse

from django.core.paginator import Paginator
# Create your views here.

# Browse jobs funcation
def job_list(request):
    jobs=Job.objects.all()
    categories=Category.objects.all()
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'Jobs':page_obj,"Categories":categories , "count":jobs.count()}

    return render(request,'jobs.html',context)

# Details page 
def job_detail(request,slug):
    job=get_object_or_404(Job,slug=slug)
    if request.method == "POST":
        apply=ApplyForm(request.POST,request.FILES)
        if apply.is_valid():
            myform=apply.save(commit=False)
            myform.job=job
            myform.save()
   
    apply=ApplyForm()
    context={'job':job,'form':apply}
    return render(request,'job_details.html',context)

# Needed to be login in to continue   
@login_required
def add_job(request):

    form=JobForm()
    if request.method == "POST":
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            slug=Job.objects.latest('published_at').slug
            return redirect("job:job_detail",slug)

    context={"form":form}
    return render(request,'add_job.html',context)