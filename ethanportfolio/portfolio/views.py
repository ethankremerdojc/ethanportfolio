from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Project

# Create your views here.
def home(request, *args, **kwargs):


    return render(request, 'portfolio/pages/home/index.html', {
        'projects': Project.all_visible()
    })