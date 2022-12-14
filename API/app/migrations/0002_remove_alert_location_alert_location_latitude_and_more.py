# Generated by Django 4.1.3 on 2022-12-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='location',
        ),
        migrations.AddField(
            model_name='alert',
            name='location_latitude',
            field=models.FloatField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert',
            name='location_longitude',
            field=models.FloatField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
