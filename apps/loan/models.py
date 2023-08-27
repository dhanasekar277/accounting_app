from django.db import models
from apps.agency.models import Agency

# Create your models here.

REPAYMENT_CHOICES = (
    ('Monthly','Monthly'),
    ('3 Months Once','3 Months Once'),
    ('6 Months Once','6 Months Once'),
)

PAYMENT_METHOD = (
    ('Cash','Cash'),
    ('Card','Card'),
    ('UPI','UPI'),
)

class Repayment(models.Model):
    Collection_Date = models.DateField()
    Payment_Method = models.CharField(max_length=5,choices=PAYMENT_METHOD)
    Collected_By = models.CharField(max_length=100)
    Amount_Paid = models.CharField(max_length=10)
    def __str__(self):
        return str(self.Collected_By)
    

class Loan(models.Model):
    Agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100) 
    Principal_Amount = models.CharField(max_length=20)
    Released_Date = models.DateField() 
    Maturity_Date = models.DateField()
    EMI_Start_Date = models.DateField()
    EMI_End_Date = models.DateField() 
    Repayment_Type = models.CharField(max_length=100,choices=REPAYMENT_CHOICES)
    Penalty = models.CharField(max_length=20)
    Interest = models.CharField(max_length=20)
    Due_Amount = models.CharField(max_length=20)
    Months_Paid = models.CharField(max_length=20, blank=True, null=True)
    Repayments = models.ManyToManyField(Repayment, blank=True)
    Date = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.Name)
    