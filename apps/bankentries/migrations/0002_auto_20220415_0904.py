# Generated by Django 3.2.12 on 2022-04-15 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
        ('customers', '0002_customer_is_active'),
        ('agency', '0003_alter_agency_date'),
        ('vendors', '0004_alter_vendor_material_supplying'),
        ('voucher', '0001_initial'),
        ('bankentries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankentry',
            old_name='Entry',
            new_name='GST_Balance_Paid',
        ),
        migrations.RenameField(
            model_name='bankentry',
            old_name='Expence_Type',
            new_name='Net_Balance_Paid',
        ),
        migrations.RemoveField(
            model_name='bankentry',
            name='GST_Balance_Amount',
        ),
        migrations.RemoveField(
            model_name='bankentry',
            name='Net_Balance_Amount',
        ),
        migrations.RemoveField(
            model_name='bankentry',
            name='Transaction_Amount',
        ),
        migrations.AddField(
            model_name='bankentry',
            name='CustomerId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='bankentry',
            name='InvoiceId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.singlesalesinvoice'),
        ),
        migrations.AddField(
            model_name='bankentry',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.agency'),
        ),
        migrations.AddField(
            model_name='bankentry',
            name='vendorId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
        migrations.AlterField(
            model_name='bankentry',
            name='voucherId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voucher.purchaseinfo'),
        ),
    ]
