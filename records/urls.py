from django.urls import path
from .views import HomeView, RecordListView, AddRecord, UpdateRecordView

app_name = 'records'
urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('list', RecordListView.as_view(), name='list' ),
    path('add/', AddRecord.as_view(), name='add' ),
    path('<pk>/update-record', UpdateRecordView.as_view(), name='update' ),
]
