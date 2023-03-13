from django.urls import path
from .views import HomeView, RecordListView, AddRecord

app_name = 'records'
urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('list', RecordListView.as_view(), name='list' ),
    path('add/', AddRecord.as_view(), name='add' ),
]
