from django.db import models

class Datos(models.Model):
    nombre = models.CharField(max_length = 10, blank=False, null=False)
    apellido = models.CharField(max_length = 10, blank=False, null=False)
    descripcion = models.TextField(max_length = 500, blank=False, null=False)
    git_hub = models.CharField(max_length = 100, blank=True, null=True)
    imagen_perfil = models.ImageField(upload_to='perfil', blank=True, null=True)

    class Meta:
        verbose_name = 'datos'
        verbose_name_plural = 'datos'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Tecnologia(models.Model):
    nombre = models.CharField(max_length = 30, blank=False, null=False)
    progreso = models.PositiveIntegerField(blank=False, null=False)


    def __str__(self):
        return self.nombre
    

class Actividad(models.Model):
    titulo = models.CharField(max_length = 50, blank=False, null=False)
    fecha = models.TimeField(blank=True, null=True)
    contenido = models.TextField(max_length = 2500, blank=False, null=False)
    link = models.CharField(max_length = 200, blank=True, null=True)
    imagen = models.ImageField(upload_to='actividad', blank=True, null=True)

    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'

    def __str__(self):
        return self.titulo






