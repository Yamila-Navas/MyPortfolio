from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('enviar-mensaje', views.enviar_mensaje, name='enviar-mensaje'),

]
