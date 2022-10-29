from django.urls import path

from . import views

app_name = 'wua'

urlpatterns = [
    path('', views.index, name='index'),
]