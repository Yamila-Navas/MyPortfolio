from django.shortcuts import render, redirect
from .models import Tecnologia, Datos, Actividad
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def index(req):
    profile = Datos.objects.get(id=1)
    project = Actividad.objects.all()
    technologies = Tecnologia.objects.all()

    ctx = {
        'profile' : profile,
        'projects': project,
        'technologies': technologies,
    }

    return render(req, 'index.html', ctx)


@csrf_exempt  # Desactiva la protección CSRF para esta vista
def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('name', '')
        email = request.POST.get('email', '')
        asunto = request.POST.get('subject', '')
        mensaje = request.POST.get('message', '')

        print('nombre: ', nombre)
        print('email: ', email)
        print('asunto: ', asunto)
        print('mensaje: ', mensaje)

        template = render_to_string('email.html', {
            'nombre': nombre,
            'mensaje': mensaje,
            'email': email
        })

        email = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['yn.yaminavas@gmail.com']
        )
        
        email.fail_silently=False
        
        email.send()

        return HttpResponse('OK')
    else:
        return HttpResponse('Ha ocurrido un error al enviar el formulario.')
