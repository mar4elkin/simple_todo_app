from django.shortcuts import render
from .models import *

def inprocces(request):
    todos = TodoObject.objects.all().filter(status="inprocces")
    #todos = TodoObject.objects.all()
    return render(request, "index.html", {"todos": todos})

def done(request):
    todos = TodoObject.objects.all().filter(status="done")
    return render(request, "index.html", {"todos": todos})