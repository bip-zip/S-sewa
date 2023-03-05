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


import qrcode
import qrcode.image.svg
from io import BytesIO
import base64

class ProfileView(TemplateView):
    template_name='user_auth/userprofile.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data(**kwargs) 
    #     context.update({"qrcode":self.get_qrcode_svg('okok')})
    #     return context
  

class QrCodeView(TemplateView):
    template_name='user_auth/qr.html'

    def get_context_data(self, **kwargs):
        context = super(QrCodeView, self).get_context_data(**kwargs)
        qrcode =  self.get_qrcode_svg('{}&{}'.format(self.request.user.id,self.request.user.email))
        context.update({"qrcode":qrcode})
        return context
    
    def get_qrcode_svg(self, text):
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(text ,image_factory=factory, box_size=30)
        stream = BytesIO()
        img.save(stream)
        base64_image = base64.b64encode(stream.getvalue()).decode()
        return 'data:image/svg+xml;utf8;base64,' + base64_image


import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import io, base64

class QrCodeScan(TemplateView):
    template_name= 'user_auth/qrscan.html'

    def post(self,request):
        # img = request.FILES['image']
        image = request.POST['image']
        image_data = base64.b64decode(image.split(',')[1])
        # create a BytesIO object from the decoded image data
        img = BytesIO(image_data)
        return HttpResponse(self.qrcodeReader(img))



    def qrcodeReader(self, img):
       
        # Read the image data using Pillow
        image = Image.open(img)
        
        # Convert the image to grayscale
        gray_image = image.convert('L')
        
        # Convert the grayscale image to a NumPy array
        np_image = np.array(gray_image)
        
        # Decode the QR code in the image using pyzbar
        decoded = decode(np_image)
        
        # Get the data from the QR code
        if len(decoded) > 0:
            data = decoded[0].data.decode('utf-8')
        else:
            data = 'No QR code found'
        
        return data
    



