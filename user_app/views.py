from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy

class UserCreateView(CreateView):
    form_class = forms.MyPersonalUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')