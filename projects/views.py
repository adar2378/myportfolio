from django.shortcuts import render
from .models import Projects
# Create your views here.


def home(request):
    projects = Projects.objects
    return render(request, 'projects/home.html', {'projects': projects})
