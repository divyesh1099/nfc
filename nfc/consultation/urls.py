from django.urls import path
from . import views
app_name='consultation'
urlpatterns=[
    path('', views.index, name='index'),
    path('virtual_consultation', views.virtual_consultation, name='virtual_consultation'),
]