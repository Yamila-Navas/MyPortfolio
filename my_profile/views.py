from django.shortcuts import render
from .models import Tecnologia, Datos, Actividad

def index(req):
    perfil = Datos.objects.get()
    actividades = Actividad.objects.all()
    tecnologias = Tecnologia.objects.all()

    ctx = {
        'perfil' : perfil,
        'actividades': actividades,
        'tecnologias': tecnologias,
    }

    return render(req, 'base.html', ctx)
