# Generated by Django 4.1.2 on 2022-11-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_ourservices_servicedesc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourservices',
            name='ServiceDesc',
        ),
        migrations.AddField(
            model_name='ourservices',
            name='serviceDesc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
