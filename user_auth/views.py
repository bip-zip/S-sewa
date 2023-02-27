from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class RegisterView(TemplateView):
    template_name='user_auth/register.html'

class SigninView(LoginView):
    template_name='user_auth/login.html'

