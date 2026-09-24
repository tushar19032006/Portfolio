from django.shortcuts import render, redirect
from .models import Project
from .mongodb import contacts

def home(request):
    # When the contact form is submitted
    if request.method == "POST":
        contacts.insert_one(
            {
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "subject": request.POST.get("subject"),
                "message": request.POST.get("message"),
            }
        )

        return redirect("home")
    
    

    # Show all projects on the homepage
    projects = Project.objects.all()

    return render(request, "home.html", {
        "projects": projects
    })