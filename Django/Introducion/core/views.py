#Se crean vistas
from django.views.generic import View
from django.shortcuts import render

#Vistas de clases
class HomeView(View):
    def get(self, request, *args,**kwargs):
        context={
            
        }
        return render(request, 'index.html', context)
        
