from django.urls import path
from .views import ArticleListView, DetailView, AddArticleView, UserArticlesView, UpdateArticleView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articlelist' ),
    path('detail/<str:slug>', DetailView.as_view(), name='articledetail' ),
    path('addarticle', AddArticleView.as_view(), name='addarticle' ),
    path('<pk>/update-article', UpdateArticleView.as_view(), name='updatearticle' ),
    path('articles', UserArticlesView.as_view(), name='articles' ),
]
