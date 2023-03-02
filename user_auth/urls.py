from django.urls import path
from .views import RegisterView, SigninView, ProfileView, QrCodeView, QrCodeScan
from django.contrib.auth import views as auth_views
from .views import *
from django.views.generic.base import RedirectView
app_name = 'user_auth'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='records:home')),
    path('signup', RegisterView.as_view(), name='register' ),      
    path('login', SigninView.as_view(), name='login' ),
     path('logout', auth_views.LogoutView.as_view(), name='logout'),      
     path('profile', ProfileView.as_view(), name='profile'),      
     path('qr', QrCodeView.as_view(), name='qr'),      
     path('qrscan', QrCodeScan.as_view(), name='qrscan'),      
]
