from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'content/projects_list.html', {'projects': projects})


def project_new(request):
    return render(request,'content/projects_new.html')

