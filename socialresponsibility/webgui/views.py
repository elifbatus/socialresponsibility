from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from .models import Project
def projectList(request):
     Projects = Project.objects.all()
     data = ""
     for element in Projects:
         data = data + "<h1>" +element.title+"</h1><p>"+element.explanation+"</p>"
     return HttpResponse(data)
