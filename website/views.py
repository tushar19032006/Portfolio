from django.shortcuts import render, redirect
from .models import Project
from .mongodb import contacts

from django.http import FileResponse, Http404 
from django.contrib.staticfiles import finders
from django.conf import settings
import os

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
    
def download_resume(request):
    resume_path = finders.find("resume.pdf")

    if not resume_path:
        raise Http404("Resume file not found")

    return FileResponse(
        open(resume_path, "rb"),
        as_attachment=True,
        filename="Tushar_Resume.pdf"
    )
    # Show all projects on the homepage
    projects = Project.objects.all()

    return render(request, "home.html", {
        "projects": projects
    })