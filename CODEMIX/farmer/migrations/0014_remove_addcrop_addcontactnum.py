# Generated by Django 3.0.4 on 2020-07-04 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0013_addcrop_addcontactnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcrop',
            name='addContactNum',
        ),
    ]
