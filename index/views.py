from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ToDo

# Create your views here.

class BlogListView(ListView):
    model = ToDo

    template_name = 'index/home.html'

class BlogDetailView(DetailView):
    model = ToDo

    template_name = 'index/post_detail.html'


class BlogCreateView(CreateView):
    model = ToDo

    template_name = 'index/post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = ToDo

    template_name = 'index/post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = ToDo

    template_name = 'index/post_delete.html'

    success_url = reverse_lazy('home')