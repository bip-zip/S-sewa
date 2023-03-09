from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import MedicationSchedule

class MedicationListView(LoginRequiredMixin,ListView):
    template_name = 'medication/medicationlist.html'
    model = MedicationSchedule
    object_name = 'object_list'
    
    def get_context_data(self, **kwargs):
        context = super(MedicationListView, self).get_context_data(**kwargs)
        obj = MedicationSchedule.objects.filter(user = self.request.user).order_by('-id') | MedicationSchedule.objects.filter(created_by = self.request.user).order_by('-id')

        context.update({ "object_list":obj, 'medication_page':'active'})
        return context
    
