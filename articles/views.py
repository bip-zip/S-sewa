from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View, ListView,CreateView
from .models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import AddArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model= Post
    template_name='articles/articlelist.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs) 
        featured = Post.objects.filter(status='published').last()
        topviews = Post.objects.filter(status='published').order_by('views').exclude(id=featured.id)[:4]
        posts = Post.objects.filter(status='published').order_by('-id').exclude(id=featured.id)
        context.update({'posts':posts, 'featured':featured,'topviewed':topviews,'article_page':'active'})
        return context


class DetailView(TemplateView):
    template_name='articles/articledetail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        post= self.kwargs['slug'] 
        obj = get_object_or_404(Post, slug=post)
        obj.views +=1
        obj.save()
        post_tags_ids = obj.tags.values_list('id', flat=True)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids,status='published').exclude(id=obj.id).distinct()
        context.update({ "post":obj, "similar_posts":similar_posts, 'article_page':'active'})
        return context

class AddArticleView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = AddArticleForm
    template_name='articles/addarticle.html'
    success_url='/articles'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = self.request.user
        messages.success(self.request,'Your article is under approval. It will be visible afterwards')
        return super().form_valid(form)
        