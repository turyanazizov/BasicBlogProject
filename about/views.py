from django.shortcuts import render

def about(request):
    return render(request,'about/about.html')

def single_project(request):
    return render(request,'about/single-project.html')