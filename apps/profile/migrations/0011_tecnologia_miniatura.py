# Generated by Django 4.2.11 on 2024-04-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0010_alter_datos_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnologia',
            name='miniatura',
            field=models.ImageField(blank=True, null=True, upload_to='miniaturas-tecnologias'),
        ),
    ]
