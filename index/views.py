from django.shortcuts import render
from django.views.generic import ListView

from .models import ToDo

# Create your views here.

class BlogListView(ListView):
    model = ToDo

    template_name = 'index/home.html'
