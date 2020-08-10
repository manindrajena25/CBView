from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView,UpdateView, DeleteView

from .models import Student, School
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'basic_app/basic_school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'basic_app/basic_school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:list')


