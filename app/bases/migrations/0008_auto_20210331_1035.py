# Generated by Django 3.1.5 on 2021-03-31 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0007_auto_20210329_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprendimiento',
            old_name='fecha_creación',
            new_name='fecha_creacion',
        ),
    ]