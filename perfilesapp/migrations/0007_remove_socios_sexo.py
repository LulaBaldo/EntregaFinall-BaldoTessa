# Generated by Django 4.0.5 on 2022-07-11 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfilesapp', '0006_alter_nosotros_options_alter_profesor_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socios',
            name='sexo',
        ),
    ]