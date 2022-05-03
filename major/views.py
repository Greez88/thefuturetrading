from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
   # ordering = ['-post_date']

class AboutView(TemplateView):
    template_name = 'aboutus.html'

class PlanView(TemplateView):
    template_name = 'plan.html'

class ServiceView(TemplateView):
    template_name = 'services.html'

class RoleView(TemplateView):
    template_name = 'rule.html'

class ContactView(TemplateView):
    template_name = 'contact.html'