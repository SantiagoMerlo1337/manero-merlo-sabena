# Generated by Django 4.1 on 2022-09-06 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_alter_viaje_user1_alter_viaje_user2'),
    ]

    operations = [
        migrations.CreateModel(
            name='DTModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('date_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
