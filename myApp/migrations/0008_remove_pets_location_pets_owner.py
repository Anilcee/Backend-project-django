# Generated by Django 4.1.4 on 2022-12-13 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0007_ourservices_servicedetails_ourservices_serviceicon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='location',
        ),
        migrations.AddField(
            model_name='pets',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
