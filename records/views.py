from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView
from .models import HealthRecord
from user_auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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
    

class UpdateRecordView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = HealthRecord
    # form_class = AddArticleForm
    fields = '__all__'
    template_name='records/updaterecords.html'
    success_url='/articles/articles'

    def test_func(self):
        return self.request.user == self.get_object().created_by
    
    

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.instance.slug = self.request.user
    #     messages.success(self.request,'Update Successful. Your article is under approval. It will be visible afterwards.')
    #     return super().form_valid(form)