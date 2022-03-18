from django.shortcuts import redirect, render
from . models import Contact

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            number=request.POST.get("number"),
            select=request.POST.get("select"),
            text=request.POST.get("text"),
            )
        return redirect('contact:contact')
    return render(request,'contact/contact.html')