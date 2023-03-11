from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import MedicationSchedule, MedicineMedicationSchedule
from user_auth.models import User
from django.http import HttpResponseRedirect

class MedicationListView(LoginRequiredMixin,ListView):
    template_name = 'medication/medicationlist.html'
    model = MedicationSchedule
    object_name = 'object_list'
    
    def get_context_data(self, **kwargs):
        context = super(MedicationListView, self).get_context_data(**kwargs)
        obj = MedicationSchedule.objects.filter(user = self.request.user).order_by('-id') | MedicationSchedule.objects.filter(created_by = self.request.user).order_by('-id')

        context.update({ "object_list":obj, 'medication_page':'active'})
        return context
    

class AddMedicationSchedule(LoginRequiredMixin,CreateView):
    template_name='medication/addmedication.html'
    model = MedicineMedicationSchedule
    fields =['medicine','desc','timesaday','emptyStomach']

    def form_valid(self, form):
        self.object = form.save(False)
        self.object.medicationSchedule = MedicationSchedule.objects.filter(created_by=self.request.user).last()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('medication:addmedication')
    
    def get_context_data(self, **kwargs):
        context = super(AddMedicationSchedule, self).get_context_data(**kwargs)
        medScd = MedicationSchedule.objects.filter(created_by = self.request.user).last()
        medicines = MedicineMedicationSchedule.objects.filter(medicationSchedule=medScd).order_by('-id')
        context.update({ "medicines":medicines})
        return context
    


def medicationScheduleCreator(request):
    user = User.object.get(id=request.GET.get('qrdata',None))
    medicationschedule = MedicationSchedule.objects.create(created_by = request.user, user=user)
    medicationschedule.save()
    return redirect ('medication:addmedication')