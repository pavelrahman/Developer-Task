# Generated by Django 2.2.1 on 2019-05-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacturer_name',
        ),
    ]
