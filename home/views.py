from multiprocessing import context
from django.shortcuts import render
from home.models import Projects,SingleProject

def home(request):
    main_content=Projects.objects.all().first()
    projects=SingleProject.objects.all()
    context={
        'main_content':main_content,
        'projects':projects,
    }
    return render(request,'home/index.html',context=context)

def single_project(request,name):
    projects=SingleProject.objects.all()
    project=projects.filter(project_name=name).first()
    context={
        'project':project,
    }
    return render(request,'home/single-project.html',context=context)