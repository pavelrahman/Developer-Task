# Generated by Django 2.2.1 on 2019-05-09 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_remove_car_manufacturer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufactormodel',
            name='car_model_image',
            field=models.FileField(default='default.jpg', upload_to='car_model_image'),
        ),
    ]
