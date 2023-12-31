# Generated by Django 3.2.12 on 2022-05-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashregister', '0002_auto_20220418_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='purchase_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity_type', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sales_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity_type', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase_entry',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchase_entry',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchase_entry',
            name='quantity_type',
        ),
        migrations.RemoveField(
            model_name='sales_entry',
            name='calculation',
        ),
        migrations.RemoveField(
            model_name='sales_entry',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sales_entry',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sales_entry',
            name='quantity_type',
        ),
        migrations.RemoveField(
            model_name='purchase_entry',
            name='material',
        ),
        migrations.RemoveField(
            model_name='sales_entry',
            name='material',
        ),
        migrations.AddField(
            model_name='purchase_entry',
            name='material',
            field=models.ManyToManyField(to='cashregister.purchase_material'),
        ),
        migrations.AddField(
            model_name='sales_entry',
            name='material',
            field=models.ManyToManyField(to='cashregister.sales_material'),
        ),
    ]
