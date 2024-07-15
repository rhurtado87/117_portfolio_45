from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects_list(request):
    
    projects = Project.objects.all()

    return render(request, 'content/projects_list.html', {'projects': projects})


def project_new(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('projects_list')

    else:
        form = ProjectForm()
    
    return render(request,'content/projects_new.html',{'form': form })

