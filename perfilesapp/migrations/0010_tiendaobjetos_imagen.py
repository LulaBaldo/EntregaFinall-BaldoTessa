# Generated by Django 4.0.1 on 2022-07-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfilesapp', '0009_alter_tiendaactividad_actividad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiendaobjetos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='objetos/', verbose_name='Imagen'),
        ),
    ]
