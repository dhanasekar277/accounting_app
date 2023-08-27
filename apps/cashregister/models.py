from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class purchase_material(models.Model):
    material=models.CharField(max_length=200,null=True,blank=True)
    quantity_type=models.CharField(max_length=200,null=True,blank=True)
    quantity=models.CharField(max_length=200,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.material)

    def natural_key(self):
        return {
            'id':self.id,
            'material':self.material,
            'quantity_type':self.quantity_type,
            'quantity':self.quantity,
            'price':self.price,
        }

class purchase_entry(models.Model):
    purchase_company=models.CharField(max_length=200,null=True,blank=True)
    sales_company=models.CharField(max_length=200,null=True,blank=True)
    billing_address=models.TextField(null=True,blank=True)
    delivery_address=models.TextField(null=True,blank=True)
    material=models.ManyToManyField(purchase_material)
    round_off=models.CharField(max_length=100,null=True,blank=True)
    total_quantity=models.CharField(max_length=100,null=True,blank=True)
    amount=models.CharField(max_length=100,null=True,blank=True)
    amount_paid=models.CharField(max_length=100,null=True,blank=True)
    amount_balance=models.CharField(max_length=100,null=True,blank=True)
    voucher=models.CharField(max_length=100,null=True,blank=True)
    dc_scan_copy=models.ImageField(upload_to='media/',null=True,blank=True)
    purchase_bill=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField()

    def __str__(self):
        return str(self.purchase_company) 

class sales_material(models.Model):
    material=models.CharField(max_length=200,null=True,blank=True)
    quantity_type=models.CharField(max_length=200,null=True,blank=True)
    quantity=models.CharField(max_length=200,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.material)

    def natural_key(self):
        return {
            'id':self.id,
            'material':self.material,
            'quantity_type':self.quantity_type,
            'quantity':self.quantity,
            'price':self.price,
        }    


class sales_entry(models.Model):
    sales_entry_date=models.DateField()
    purchase_company=models.CharField(max_length=200,null=True,blank=True)
    sales_company=models.CharField(max_length=200,null=True,blank=True)
    billing_address=models.TextField(null=True,blank=True)
    delivery_address=models.TextField(null=True,blank=True)
    material=models.ManyToManyField(sales_material)
    round_off=models.CharField(max_length=100,null=True,blank=True)
    total_quantity=models.CharField(max_length=100,null=True,blank=True)
    amount=models.CharField(max_length=100,null=True,blank=True)
    amount_paid=models.CharField(max_length=100,null=True,blank=True)
    amount_balance=models.CharField(max_length=100,null=True,blank=True)
    invoice=models.CharField(max_length=100,null=True,blank=True)
    dc_scan_copy=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return str(self.purchase_company)


class CashUser(models.Model):
    Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    # def save(self, *args, **kwargs):
    #     self.Password = make_password(self.Password)
    #     super(CashUser, self).save(*args, **kwargs)