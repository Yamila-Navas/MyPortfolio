# Generated by Django 4.2.11 on 2024-04-11 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0007_actividad_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]