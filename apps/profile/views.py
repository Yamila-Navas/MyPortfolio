from django.shortcuts import render
from .models import Tecnologia, Datos, Actividad



def index(req):
    profile = Datos.objects.get(id=1)
    technologies = Tecnologia.objects.all()
    main_project = Actividad.objects.get(titulo = 'Code Trivia Game')
    project = Actividad.objects.exclude(titulo = 'Code Trivia Game').order_by('-id')
    

    print(main_project)

    ctx = {
        'profile' : profile,
        'technologies': technologies,
        'main_project' : main_project,
        'projects': project,
    }

    return render(req, 'index.html', ctx)