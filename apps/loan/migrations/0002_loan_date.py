# Generated by Django 4.0.1 on 2022-03-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]
