# Generated by Django 3.2.12 on 2022-04-01 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_notification_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemanagement',
            name='File',
            field=models.FileField(upload_to='uploads/% Y/% m/% d/'),
        ),
    ]