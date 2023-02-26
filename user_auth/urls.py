from django.urls import path
from .views import RegisterView, SigninView
from django.contrib.auth import views as auth_views

app_name = 'user_auth'
urlpatterns = [
    path('signup', RegisterView.as_view(), name='register' ),      
    path('login', SigninView.as_view(), name='login' ),
     path('logout', auth_views.LogoutView.as_view(), name='logout'),      
]
