# Generated by Django 4.2.11 on 2024-03-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_alter_actividad_options_alter_datos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='actividad'),
        ),
    ]