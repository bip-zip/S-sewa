from django.views.generic import TemplateView, View, ListView
from .models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib import messages
from django.shortcuts import get_object_or_404

class ArticleListView(ListView):
    model= Post
    template_name='articles/articlelist.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs) 
        featured = Post.objects.last()
        topviews = Post.objects.order_by('views').exclude(id=featured.id)[:4]
        posts = Post.objects.all().order_by('-id').exclude(id=featured.id)
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
        similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=obj.id).distinct()
        context.update({ "post":obj, "similar_posts":similar_posts, 'article_page':'active'})
        return context

