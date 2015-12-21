from django.shortcuts import render

# Create your views here.
from .models import Project
def projectList(request):
     Projects = Project.objects.all()
     return render(request, 'projects.html', {'projects':Projects})
