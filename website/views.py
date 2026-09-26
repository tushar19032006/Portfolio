from django.shortcuts import render, redirect
from .models import Project
from .mongodb import contacts

from django.http import FileResponse
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
    resume_path = os.path.join(settings.BASE_DIR, "website", "static", "resume.pdf")
    return FileResponse(open(resume_path, "rb"), as_attachment=True, filename="Tushar_Resume.pdf")

    # Show all projects on the homepage
    projects = Project.objects.all()

    return render(request, "home.html", {
        "projects": projects
    })