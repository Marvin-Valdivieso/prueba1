# Generated by Django 3.1.5 on 2021-03-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprendedor',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='instragram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='emprendimiento',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Descripción del Emprendimiento', max_length=500, null=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Descripción del Producto', max_length=500, null=True, verbose_name='descripción'),
        ),
    ]
