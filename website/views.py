from django.shortcuts import render, redirect
from .models import Project
from .mongodb import contacts
from django.core.mail import send_mail

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
        send_mail(
            subject=f"Portfolio Contact: {request.POST.get('subject')}",
            message=f"""
    Name: {request.POST.get('name')}
    Email: {request.POST.get('email')}

    Message:
    {request.POST.get('message')}
    """,
            from_email=None,
            recipient_list=["yourgmail@gmail.com"],   # Replace with your Gmail
            fail_silently=False,
        )

        return redirect("home")
    
    

    # Show all projects on the homepage
    projects = Project.objects.all()

    return render(request, "home.html", {
        "projects": projects
    })