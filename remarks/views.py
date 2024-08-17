from django.shortcuts import render
from django.views.generic import ListView, CreateView
# 'reverse_lazy' reverses and resolves URLs when its needed
from django.urls import reverse_lazy

from .models import Remark
from .form import RemarkForm

# Create your views here.
class HomePageView(ListView):
    model = Remark
    template_name = 'home.html'

#view to allow users to upload new images 'form.py'
class CreateRemarkView(CreateView):
    model = Remark
    template_name = 'remark.html'
    form_class = RemarkForm
    success_url = reverse_lazy('home')