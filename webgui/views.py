from django.shortcuts import render

# Create your views here.

def projectList(request):
     return render(request, 'projects.html', {})
