from multiprocessing import context
from django.shortcuts import render
from . models import Blog

def blog(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request,'blog/blog.html',context=context)

def single_post(request,name):
    blog=Blog.objects.all().filter(creator_name=name).first()
    context={
        'blog':blog
    }
    return render(request,'blog/single-post.html',context=context)