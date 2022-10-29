from django.shortcuts import render
from django.views.generic import TemplateView
from .models import tugas4

class WuaView(TemplateView):
    template_name ='tugas4/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = tugas4.objects.all()
        return context
    
    

