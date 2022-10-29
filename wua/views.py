from django.shortcuts import render
from .models import divisi, tanggal, activity

def index(request):
    divisi_list = divisi.objects.all()
    tanngal_list = tanggal.objects.all()
    activity_list = activity.objects.all()
    context = {
        'divisi': divisi_list,
        'tanggal': tanngal_list,
        'activity': activity_list
    }
    
    return render(request, 'wua/index.html', context)

# Create your views here.
