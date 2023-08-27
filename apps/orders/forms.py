from django.core import validators
from django import forms
from django.db.models import fields
from django.db.models.fields.files import FileField
from django.forms import widgets
from apps.orders import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import FormActions
 
class MaterialOrderForm(forms.ModelForm):
    class Meta:
        model = models.MaterialOrder
        fields = '__all__'
        widgets = {
            'Others': forms.Textarea(attrs={'class':'form-control ', 'rows':'1'}),
            'Expected_Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Vendor': forms.TextInput(attrs={'class':'form-control ','value':'', 'type':'hidden'}),
        }

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Row(

            Column('Material_Name', css_class="col-md-4 mt-1"),
            Column('Offer_Price', css_class="col-md-2 ps-0 mt-1"),
            Column('No_Of_Load', css_class="col-md-1 ps-0 mt-1"),
            Column('Quantity', css_class="col-md-1 ps-0 mt-1"),
            Column('HSNCode', css_class="col-md-2 ps-0 mt-1"),
            Column('Expected_Date', css_class="col-md-3 mt-1"),
            Column('Quality_Material_Type', css_class="col-md-3 ps-0 mt-1"),
            Column('Moisture', css_class="col-md-1 ps-0 mt-1"),
            Column('Moisture_Number', css_class="col-md-3 ps-0 mt-1"),
            Column('Material_Term', css_class="col-md-2 ps-0 mt-1"),
            Column('Others', css_class="col-md-12 mt-1"),
            css_class='form-row row'
        ),
        FormActions(
            Submit('add_material', 'Add Material', css_class="mt-2  btn-sm"),
            css_class='form-row add_agencies'
        )
    )


