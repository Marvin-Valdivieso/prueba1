# Generated by Django 3.1.5 on 2021-03-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0004_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='Asunto',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]