# Generated by Django 4.0.1 on 2022-03-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialorder',
            name='Others',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ponumber',
            name='Remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
