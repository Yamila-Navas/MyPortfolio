# Generated by Django 4.2.11 on 2024-04-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0011_tecnologia_miniatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='link_articulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]