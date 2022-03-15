from django.shortcuts import render
from about.models import AboutMain,AboutSubject

def about(request):
    main=AboutMain.objects.all().first()
    subjects=AboutSubject.objects.all()
    context={
        'main':main,
        'subjects':subjects
    }

    return render(request,'about/about.html',context=context)