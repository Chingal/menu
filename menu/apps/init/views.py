from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Menu
from django.contrib.auth.views import login

class IndexView(TemplateView):
    template_name = 'init/index.html'

class MenuListView(ListView):
    model = Menu
    context_object_name = 'opciones'
    queryset = Menu.objects.all()
    template_name = 'base.html'