# Generated by Django 3.2.8 on 2022-03-02 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_From',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('Q', 'Quarry Owner'), ('T', 'Transport Owner'), ('C', 'Crusher Owner')], default=1, max_length=1)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material_Supplying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Material_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Material_GST', models.CharField(blank=True, max_length=20, null=True)),
                ('HSNCode', models.CharField(blank=True, max_length=20, null=True)),
                ('Material_Type', models.CharField(blank=True, choices=[('N', 'Natural'), ('M', 'Manufactured')], default=1, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material_To',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quality', models.CharField(blank=True, max_length=30, null=True)),
                ('Price', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VendorCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_Certificate_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Vendor_Certificate_Scan_Copy', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='VendorGST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leggal_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Trade_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Holder_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('GST_No', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
                ('Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Email', models.CharField(blank=True, max_length=40, null=True)),
                ('Bank_Account', models.CharField(blank=True, max_length=40, null=True)),
                ('Account_Number', models.CharField(blank=True, max_length=40, null=True)),
                ('IFSC', models.CharField(blank=True, max_length=40, null=True)),
                ('Branch', models.CharField(blank=True, max_length=40, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=30, null=True)),
                ('State', models.CharField(blank=True, max_length=30, null=True)),
                ('Zip', models.CharField(blank=True, max_length=20, null=True)),
                ('Country', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorGSTBankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('Zip', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorPAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PAN_No', models.CharField(blank=True, max_length=100, null=True)),
                ('PAN_Scan_Copy', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='VendorStaffDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(blank=True, max_length=50, null=True)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Photo', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('Address', models.TextField(blank=True, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('Country', models.CharField(blank=True, max_length=50, null=True)),
                ('Zip', models.TextField(blank=True, null=True)),
                ('Published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorTIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIN_No', models.CharField(blank=True, max_length=100, null=True)),
                ('TIN_Scan_Copy', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_Type', models.CharField(blank=True, choices=[('0', 'GST User'), ('1', 'Unregistered User')], default=1, max_length=1, null=True)),
                ('Vendor_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Company_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Photo', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Zip', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Vendor_Category', models.CharField(blank=True, choices=[('Q', 'Quarry Owner'), ('T', 'Transport Owner'), ('C', 'Crusher Owner')], max_length=1, null=True)),
                ('No_Of_Trucks', models.CharField(blank=True, max_length=100, null=True)),
                ('Payment_Capabilities', models.CharField(blank=True, max_length=100, null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('Agency', models.ManyToManyField(blank=True, to='agency.Agency')),
                ('Certificate', models.ManyToManyField(blank=True, to='vendors.VendorCertificate')),
                ('GST_No', models.ManyToManyField(blank=True, to='vendors.VendorGST')),
                ('Material_From', models.ManyToManyField(blank=True, to='vendors.Material_From')),
                ('Material_Supplying', models.ManyToManyField(blank=True, null=True, to='vendors.Material_Supplying')),
                ('Material_To', models.ManyToManyField(blank=True, to='vendors.Material_To')),
                ('PAN_No', models.ManyToManyField(blank=True, to='vendors.VendorPAN')),
                ('TIN_No', models.ManyToManyField(blank=True, to='vendors.VendorTIN')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Vendor_Staff_Detail', models.ManyToManyField(blank=True, to='vendors.VendorStaffDetail')),
            ],
        ),
        migrations.AddField(
            model_name='material_to',
            name='SubLocation',
            field=models.ManyToManyField(blank=True, to='vendors.Sub_Location'),
        ),
        migrations.AddField(
            model_name='material_supplying',
            name='Quality',
            field=models.ManyToManyField(blank=True, to='vendors.MaterialQuality'),
        ),
    ]
