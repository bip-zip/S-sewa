from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class MedicationListView(LoginRequiredMixin,TemplateView):
    template_name = 'medication/medicationlist.html'
