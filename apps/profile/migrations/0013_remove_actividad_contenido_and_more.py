# Generated by Django 4.2.11 on 2024-04-14 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0012_actividad_link_articulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='datos',
            name='imagen_perfil',
        ),
        migrations.RemoveField(
            model_name='tecnologia',
            name='progreso',
        ),
    ]