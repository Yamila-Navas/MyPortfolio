# Generated by Django 4.2.11 on 2024-03-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_alter_actividad_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fecha',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
