from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, CreateView
from .models import HealthRecord
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HealthRecord
from user_auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages



class HomeView(TemplateView):
    template_name='records/home.html'

class RecordListView(ListView):
    template_name = 'records/list.html'
    model = HealthRecord

    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        obj = HealthRecord.objects.filter(user = self.request.user).order_by('-id') | HealthRecord.objects.filter(created_by = self.request.user).order_by('-id')
        context.update({ "object_list":obj, 'history_page':'active'})
        return context


class AddRecord(LoginRequiredMixin,CreateView):
    template_name='records/addrecords.html'
    model = HealthRecord
    fields =["prescription",'documents','status','end_date']


    def form_valid(self, form):
        self.object = form.save(False)
        user = User.object.get(id=self.request.GET.get('qrdata',None))
        self.object.user = user
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    
    def get_success_url(self):
        messages.success(self.request,'Record added successfully.')
        return reverse('records:add')
    
    # def get_context_data(self,request, **kwargs):
    #     context = super(AddRecord, self).get_context_data(**kwargs)
    #     user = User.object.get(id=request.GET.get('qrdata',None))
    #     medicationschedule = MedicationSchedule.objects.create(created_by = request.user, user=user)
    #     context.update({ "medicines":medicines})
    #     return context