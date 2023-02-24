from django.shortcuts import render
from django.views.generic import TemplateView, View

class RegisterView(TemplateView):
    template_name='user_auth/register.html'

class LoginView(TemplateView):
    template_name='user_auth/login.html'