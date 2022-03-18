from django.shortcuts import render, redirect
from . models import Blog, Comment


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context=context)


def single_post(request, name):
    blog = Blog.objects.all().filter(creator_name=name).first()
    comments = Blog.objects.all().filter(creator_name=name).first().koments.filter(status='Approve')
    context = {
        'blog': blog,
        'comments': comments
    }
    if request.method == "POST":
        Comment.objects.create(
            blog=Blog.objects.all().filter(creator_name=name).first(),
            text=request.POST.get("text"),
            name=request.POST.get("name"),
            email=request.POST.get("email"),
        )
    return render(request, 'blog/single-post.html', context=context)
