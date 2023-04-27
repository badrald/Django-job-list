from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .form import BlogCreateForm
from .models import Profile,Blog
from django.core.paginator import Paginator
# Create your views here.


def blogs(request):
    blogs=Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'blogs':page_obj}
    return render(request,'blog/blogs.html',context)



def single_blog(request,slug):
    blog=Blog.objects.get(slug=slug)
    context={'blog':blog}
    return render(request,'blog/single-blog.html',context)

@login_required
def blog_create(request):
    if request.method == 'POST':
        form=BlogCreateForm(request.POST,request.FILES)
        if form.is_valid:
            myform=form.save(commit=False)
            myform.profile=get_object_or_404(Profile,user=request.user)
            myform.save()
            return redirect('blog:single_blog',myform.slug)
    else :
        form=BlogCreateForm()
        return render(request,'blog/blog_create.html',{'form':form})