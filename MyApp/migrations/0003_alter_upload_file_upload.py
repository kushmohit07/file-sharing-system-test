# Generated by Django 4.2.7 on 2024-01-05 17:24

import MyApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_file',
            name='upload',
            field=models.FileField(upload_to='file/', validators=[MyApp.models.validate_file_extension]),
        ),
    ]
