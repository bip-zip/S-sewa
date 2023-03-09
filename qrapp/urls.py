from django.urls import path
from .views import  QrCodeView, QrCodeScan
app_name = 'qrapp'
urlpatterns = [
    path('qr', QrCodeView.as_view(), name='qr'),      
     path('qrscan', QrCodeScan.as_view(), name='qrscan'),      
]