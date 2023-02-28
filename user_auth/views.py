from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegisterForm
from .models import User
from django.contrib.auth import login as auth_login
from django.shortcuts import render, HttpResponseRedirect

class SigninView(LoginView):
    template_name='user_auth/login.html'
    success_message = "You were successfully logged in."

    def form_valid(self, form):
        user = form.get_user()
        employee = User.objects.get(email=user.email)
        if employee.user_confirmed:
            auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())



class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'user_auth/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account successfully created.')
            return redirect('user_auth:login')
        return render(request, self.template_name, {'form':form})