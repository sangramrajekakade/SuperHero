from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
class HomePage(TemplateView):
    template_name = 'flash/index.html'
