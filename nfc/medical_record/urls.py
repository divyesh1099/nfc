from django.urls import path
from . import views
app_name='medical_record'
urlpatterns = [
    path('<int:patient_id>/', views.index, name='index'),
    path('download/<str:record_number>/', views.download_medical_record, name='download_medical_record'),
]