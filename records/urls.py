from django.urls import path
from .views import HomeView, RecordListView

app_name = 'records'
urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('list', RecordListView.as_view(), name='list' ),
]
