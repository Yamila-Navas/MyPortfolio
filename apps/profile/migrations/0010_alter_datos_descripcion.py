# Generated by Django 4.2.11 on 2024-04-11 23:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_alter_actividad_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
