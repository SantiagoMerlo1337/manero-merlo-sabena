# Generated by Django 4.1 on 2022-09-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0007_delete_dtmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
