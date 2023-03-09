from django.http import HttpResponse
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
        if employee.is_superuser :
            auth_login(self.request, form.get_user())
            messages.success(self.request,'Logged in as a superuser.')
            return redirect('/admin')
        elif employee.user_verification and employee.is_patient:
            auth_login(self.request, form.get_user())
            messages.success(self.request,'Logged in as {}.'.format(employee.username))
            return redirect('user_auth:profile')
        elif employee.user_verification and employee.is_institution:
            auth_login(self.request, form.get_user())
            messages.success(self.request,'Logged in as {}.'.format(employee.email))
            return redirect('user_auth:profile')
        elif not employee.user_verification:
            messages.error(self.request, "Account may be under verificaton.")
            return redirect('user_auth:login')
        else:
            messages.error(self.request, "Something went wrong. ")

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
            messages.success(request, 'Account successfully created. You will bea able to login after the verification.')
            return redirect('user_auth:login')
        return render(request, self.template_name, {'form':form})



class ProfileView(TemplateView):
    template_name='user_auth/userprofile.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data(**kwargs) 
    #     context.update({"qrcode":self.get_qrcode_svg('okok')})
    #     return context
  

