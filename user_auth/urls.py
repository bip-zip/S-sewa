from django.urls import path
from .views import RegisterView, SigninView

app_name = 'user_auth'
urlpatterns = [
    path('signup', RegisterView.as_view(), name='register' ),      
    path('login', SigninView.as_view(), name='login' ),      
]
