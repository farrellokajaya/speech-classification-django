"""speechclassification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from todo.viewset_api import *
from tugas4.views import WuaView

router = routers.DefaultRouter()
router.register('todo', TaskViewset)


urlpatterns = [ 
    path('', RedirectView.as_view(url='/dashboard'), name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('grade/', include('grade.urls')),
    path('audio/', include('audio.urls')),
    path('transcribe/', include('transcribe.urls')),
    path('admin/', admin.site.urls),   
    path('tugas2/', include('tugas.urls')),
    path('todo/', include('todo.urls')),
    path('api/', include(router.urls)),
    path('tugas4/', WuaView.as_view(), name='wua'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
