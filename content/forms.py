from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        field = ['name','description','year', 'image', 'repository', '']

        widget = {
            'name': forms.TextInput(attrs={'placeholder': 'Project Name'}),

            'description': forms.Textarea(attrs={'placeholder': 'Description'}),

            'year': forms.NumberInput(attrs={'placeholder': 'YYYY'}),

            'image': forms.ClearableFileInput(attrs={'placeholder': 'Selecet an Image'}),

            'repository': forms.URLInput(attrs={'placeholder': 'GitHub URL'})


        }