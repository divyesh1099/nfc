from django.urls import path
from . import views
app_name='patient'
urlpatterns=[
    path('', views.index, name='index'),
    path('view_medical_records', views.view_medical_records, name='view_medical_records'),
]