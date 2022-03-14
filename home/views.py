from django.shortcuts import render

def home(request):
    return render(request,'home/index.html')

def single_project(request):
    return render(request,'home/single-project.html')