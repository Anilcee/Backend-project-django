# Generated by Django 4.1.4 on 2022-12-13 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_remove_pets_location_pets_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
    ]
