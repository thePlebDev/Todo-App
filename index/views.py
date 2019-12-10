from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ToDo

# Create your views here.

class BlogListView(ListView):
    model = ToDo

    template_name = 'index/home.html'

class BlogDetailView(DetailView):
    model = ToDo

    template_name = 'index/post_detail.html'


