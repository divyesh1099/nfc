from django.urls import path
from . import views
app_name='appointment'
urlpatterns=[
    path('', views.index, name='index'),
    path('schedule_appointment', views.schedule_appointment, name='schedule_appointment'),
]