from django.views.generic import TemplateView, View
from .models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse

class ArticleView(TemplateView):
    template_name='articles/list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs) 
        featured = Post.objects.last()
        topviews = Post.objects.order_by('views').exclude(id=featured.id)[:4]
        object_list = Post.objects.all().order_by('-id').exclude(id=featured.id)
        paginator = Paginator(object_list, 12)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context.update({ "posts":posts,'page':page,'featured':featured,'topviewed':topviews, 'categories':categories,'article_page':'active'})
        return context


class CategoryView(TemplateView):
    template_name='articles/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs) 
        slug= self.kwargs['slug']
        cat = Category.objects.get(slug=slug)
        object_list = Post.objects.filter(category=cat)
        paginator = Paginator(object_list, 12)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context.update({ "posts":posts,'page':page,'category':cat.category,'article_page':'active'})
        return context

class DetailView(TemplateView):
    template_name='articles/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        post= self.kwargs['slug'] 
        obj = get_object_or_404(Post, slug=post)
        obj.views +=1
        obj.save()
        post_tags_ids = obj.tags.values_list('id', flat=True)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=obj.id).distinct()
        context.update({ "post":obj, "similar_posts":similar_posts, 'article_page':'active'})
        return context

