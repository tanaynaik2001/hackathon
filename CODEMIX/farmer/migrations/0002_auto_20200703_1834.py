# Generated by Django 3.0.4 on 2020-07-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcrop',
            name='addCropImg',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]