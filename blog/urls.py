from django.urls import path

from . import views

app_name='blog'

urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('blog/<str:slug>',views.single_blog,name='single_blog'),
    path('create/',views.blog_create,name='blog_create')
]
