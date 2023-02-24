from django.shortcuts import render
from django.views.generic import TemplateView, View

class HomeView(TemplateView):
    template_name='records/home.html'

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs) 
    #     context.update({ "posts":posts,'page':page,'featured':featured,'topviewed':topviews, 'categories':categories,'article_page':'active'})
    #     return context