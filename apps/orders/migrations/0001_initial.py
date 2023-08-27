# Generated by Django 3.2.8 on 2022-03-02 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0001_initial'),
        ('products', '0001_initial'),
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Location_Supply', models.CharField(blank=True, max_length=100, null=True)),
                ('Delivery_Site', models.CharField(blank=True, default='AT SITE', max_length=100, null=True)),
                ('Payment_Capability', models.CharField(blank=True, max_length=100, null=True)),
                ('Material_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Expected_Date', models.DateField()),
                ('Quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity_Type', models.CharField(blank=True, choices=[('0', 'NO'), ('1', 'MT'), ('2', 'CFT'), ('4', 'QF'), ('5', 'M3'), ('6', 'QM'), ('7', 'Cage'), ('8', 'KG')], default=0, max_length=1, null=True)),
                ('Load', models.CharField(blank=True, max_length=50, null=True)),
                ('Current_Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Sale_Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Purchase_Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Fianl_PO_Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Final_Purchase_Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Final_Offer_Price', models.CharField(blank=True, max_length=50, null=True)),
                ('HSNCode', models.CharField(blank=True, max_length=50, null=True)),
                ('Quality_Material_Type', models.CharField(blank=True, choices=[('N', 'Natural'), ('M', 'Manufactured')], default=1, max_length=1, null=True)),
                ('Moisture', models.CharField(blank=True, choices=[('1', 'Yes'), ('0', 'No')], default=1, max_length=1, null=True)),
                ('Moisture_Number', models.CharField(blank=True, max_length=50, null=True)),
                ('Purchase_Entry', models.BooleanField(default=False)),
                ('Sale_Entry', models.BooleanField(default=False)),
                ('Material_Term', models.CharField(blank=True, max_length=100, null=True)),
                ('Others', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='POMaterialInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Material_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('Quantity_Type', models.CharField(choices=[('0', 'NO'), ('1', 'MT'), ('2', 'CFT'), ('4', 'QF'), ('5', 'M3'), ('6', 'QM'), ('7', 'Cage'), ('8', 'KG')], default=0, max_length=1)),
                ('Load', models.CharField(blank=True, max_length=20, null=True)),
                ('PO_Rate', models.CharField(blank=True, max_length=50, null=True)),
                ('Moisture', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], default=0, max_length=1)),
                ('Moisture_No', models.CharField(default=0, max_length=30)),
                ('PO_Terms', models.CharField(blank=True, max_length=100, null=True)),
                ('Published', models.DateTimeField(auto_now_add=True)),
                ('Material_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='PONumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PO_Type', models.CharField(choices=[('PA', 'PO Applicable'), ('NA', 'Not Applicable')], max_length=2)),
                ('PO_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Scan_Copy', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('PO_Reciver_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('PO_Reciver_Mail', models.CharField(blank=True, max_length=50, null=True)),
                ('PO_Approved_By', models.CharField(blank=True, max_length=50, null=True)),
                ('PO_Date', models.DateField(blank=True, null=True)),
                ('Order_Recieved_Date', models.DateField(blank=True, null=True)),
                ('Order_Expected_Date', models.DateField(blank=True, null=True)),
                ('Remarks', models.TextField()),
                ('PO_Material_Info', models.ManyToManyField(blank=True, to='orders.POMaterialInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sales_Delivery_Address', models.TextField()),
                ('Billing_Address', models.TextField()),
                ('Approved', models.BooleanField(default=False)),
                ('SalesApproved', models.BooleanField(default=False)),
                ('Agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.agency')),
                ('Materials', models.ManyToManyField(to='orders.MaterialOrder')),
                ('PO_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ponumber')),
                ('Sales_Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='materialorder',
            name='Mat_PO_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.pomaterialinfo'),
        ),
        migrations.AddField(
            model_name='materialorder',
            name='Product_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='materialorder',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='materialorder',
            name='Vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
    ]
