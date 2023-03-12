from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from .models import HealthRecord

class HomeView(TemplateView):
    template_name='records/home.html'



    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs) 
    #     context.update({ "posts":posts,'page':page,'featured':featured,'topviewed':topviews, 'categories':categories,'article_page':'active'})
    #     return context


class RecordListView(ListView):
    template_name = 'records/list.html'
    model = HealthRecord

    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        obj = HealthRecord.objects.filter(user = self.request.user).order_by('-id') | HealthRecord.objects.filter(created_by = self.request.user).order_by('-id')
        context.update({ "object_list":obj, 'history_page':'active'})
        return context
