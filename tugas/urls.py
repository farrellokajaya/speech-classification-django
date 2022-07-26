from django.urls import path

from . import views

app_name = 'tugas'

urlpatterns = [
    path('', views.index, name='index'),
]