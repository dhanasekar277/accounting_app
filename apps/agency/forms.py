from django.core import validators
from django import forms
from django.db.models import fields
from django.db.models.fields.files import FileField
from django.forms import widgets
from apps.agency import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import FormActions
 
class AgencyForm(forms.ModelForm):
    class Meta:
        model = models.Agency
        fields = '__all__'
        widgets = { 
            'Logo': forms.FileInput(attrs={'class':'form-control ', 'required': False, }),
            'User': forms.TextInput(attrs={'class':'form-control ','value':'', 'type':'hidden'}),
            'Name': forms.TextInput(attrs={'class':'form-control ', 'required': True, 'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            'Email': forms.TextInput(attrs={'class':'form-control ', 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
            'GST_Number': forms.TextInput(attrs={'class':'form-control ', 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Gst number does not contain special charecters and space'}),
            'PAN_Number': forms.TextInput(attrs={'class':'form-control ', 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Pan number does not contain special charecters and space'}),
            'Tin': forms.TextInput(attrs={'class':'form-control ', 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Tin number does not contain special charecters and space'}),
            'Location_Url': forms.TextInput(attrs={'class':'form-control ', 'pattern':"^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$", 'title':'Please enter valid url'}),
            'City': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'City contains alphabets only'}),
            'Zip': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^\d{6}$', 'title':'Zip contains six numbers only'}),
            'State': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'State contains alphabets only'}),
            'Country': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'Country contains alphabets only'}),
        }

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Row(
            Column('Name', css_class="col-md-4 pe-0"),
            Column('Email', css_class="col-md-4 pe-0"),
            Column('Logo', css_class="col-md-4 "),
            Column('GST_Number', css_class="col-md-3 my-2 pe-0"),
            Column('PAN_Number', css_class="col-md-3 my-2 pe-0"),
            Column('Tin', css_class="col-md-3 my-2 pe-0"),
            Column('Location_Url', css_class="col-md-3 my-2 "),
            Column('Address', css_class="col-md-5 pe-0"),
            Column('City', css_class="col-md-2 pe-0"),
            Column('Zip', css_class="col-md-1 pe-0"),
            Column('State', css_class="col-md-2 pe-0"),
            Column('Country', css_class="col-md-2 "),
            Column('User', css_class="col-md-12 pe-0"),
            Column('Phone', css_class="col-md-4 pe-0 mt-2 d-none"),
            Column('Bank_Account', css_class="col-md-4 pe-0 mt-2 d-none"),
            Column('Certificates', css_class="col-md-4 mt-2 d-none"),
            css_class='form-row row'
        ),
        FormActions(
            Submit('add_agency', 'Add Agency', css_class="mt-3  btn-sm"),
            css_class='form-row add_agencies'
        )
    )

