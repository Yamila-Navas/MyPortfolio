from django.db import models
from ckeditor.fields import RichTextField

class Datos(models.Model):
    nombre = models.CharField(max_length = 10, blank=False, null=False)
    apellido = models.CharField(max_length = 10, blank=False, null=False)
    descripcion = RichTextField()
    git_hub = models.CharField(max_length = 150, blank=True, null=True)
    linkedin = models.CharField(max_length = 200, blank=True, null=True)
    cv = models.FileField(upload_to='pdfs', blank=True, null=True)

    class Meta:
        verbose_name = 'datos'
        verbose_name_plural = 'datos'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Tecnologia(models.Model):
    nombre = models.CharField(max_length = 30, blank=False, null=False)
    miniatura = models.ImageField(upload_to='miniaturas-tecnologias', blank=True, null=True)
    


    def __str__(self):
        return self.nombre
    

class Actividad(models.Model):
    titulo = models.CharField(max_length = 50, blank=False, null=False)
    fecha = models.TimeField(blank=True, null=True)
    descripcion = RichTextField()
    git_hub = models.CharField(max_length = 200, blank=True, null=True)
    web = models.CharField(max_length = 200, blank=True, null=True)
    articulo = models.CharField(max_length = 200, blank=True, null=True)
    imagen = models.ImageField(upload_to='actividad', blank=True, null=True)

    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'

    def __str__(self):
        return self.titulo






