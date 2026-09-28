from django.shortcuts import render, redirect
from .models import Project
from .mongodb import contacts

from django.http import FileResponse, Http404 
from django.contrib.staticfiles import finders
from django.conf import settings
import os

from pymongo.errors import PyMongoError
from django.contrib import messages

def home(request):
    if request.method == "POST":
        try:
            contacts.insert_one({
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "subject": request.POST.get("subject"),
                "message": request.POST.get("message"),
            })
            messages.success(request, "Message sent successfully!")
            
        except Exception as e:
            print("FULL MONGODB ERROR:", repr(e))
            messages.error(request, "Unable to send message right now.")

        return redirect("home")

    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

