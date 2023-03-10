from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
import qrcode
import qrcode.image.svg
from io import BytesIO
import base64
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
from django.contrib import messages
from django.http import HttpResponse
from user_auth.models import User
from django.http import HttpResponseRedirect
class QrCodeView(TemplateView):
    
    template_name='qrapp/qr.html'

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


class QrCodeScan(TemplateView):
    template_name= 'qrapp/qrscan.html'

    def post(self,request, action):
        image = request.POST['image']
        image_data = base64.b64decode(image.split(',')[1])

        img = BytesIO(image_data)
        data = self.qrcodeReader(img)
        if data == False :
            messages.error(request, 'Invalid QR code.')
            return HttpResponseRedirect(self.request.path_info)
        try:
            User.object.filter(id=data.split('&')[0]).exists()
        except ValueError:
            messages.error(request, 'Invalid QR code.')
            return HttpResponseRedirect(self.request.path_info)
        if action == 'medicationschedule':
            return redirect("/medications/medicationcreate/?qrdata={}".format(data.split('&')[0]))
        elif action == 'records' :
            return redirect("/records/add/?qrdata={}".format(data.split('&')[0]))
    

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
            data = False
        return data
        
    



