from django.core import validators
from django import forms
from django.db.models import fields
from django.db.models.fields.files import FileField
from django.forms import widgets
from apps.customers import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import FormActions


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"
        widgets = {
            "User": forms.TextInput(
                attrs={"class": "form-control ", "value": "", "type": "hidden"}
            ),
            "Founder_Address": forms.Textarea(
                attrs={"class": "form-control ", "rows": "1"}
            ),
            "Remarks": forms.Textarea(attrs={"class": "form-control ", "rows": "1"}),
            "PAN_Scan_Copy": forms.FileInput(
                attrs= {
                    "class": "form-control ",
                    "required": False,
                }
            ),
            "Company_Name": forms.TextInput(attrs={"class": "form-control "}),
            "Founder_Name": forms.TextInput(attrs={"class": "form-control ", 'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            'Company_Address': forms.TextInput(attrs={'class':'form-control ', 'style':'height:38px'}),
            'Company_City': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'City contains alphabets only'}),
            'Company_Zip': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^\d{6}$', 'title':'Zip contains six numbers only'}),
            'Company_State': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'State contains alphabets only'}),
            'Company_Country': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'Country contains alphabets only'}),
            'Founder_City': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'City contains alphabets only'}),
            'Founder_Zip': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^\d{6}$', 'title':'Zip contains six numbers only'}),
            'Founder_State': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'State contains alphabets only'}),
            'Founder_Country': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'Country contains alphabets only'}),
            "Founder_Email": forms.TextInput(attrs={"class": "form-control ", 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
            'delivery_City': forms.TextInput(attrs={'class':'form-control', 'pattern':'^[A-Za-z_ ]+', 'title':'City contains alphabets only'}),
            'delivery_Zip': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^\d{6}$', 'title':'Zip contains six numbers only'}),
            'delivery_State': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'State contains alphabets only'}),
            'delivery_Country': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'Country contains alphabets only'}),
            'delivery_Address': forms.TextInput(attrs={'class':'form-control', 'style':'height:38px'}),
            # "Company_Email": forms.TextInput(attrs={"class": "form-control ", 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
            # "Founder_Phone": forms.TextInput(attrs={"class": "form-control ", 'required': True,'pattern':'^\d{10}$', 'title':'Enter your valid 10 digit mobile number'}),
            # "GST_No": forms.TextInput(attrs={"class": "form-control ", 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Gst number does not contain special charecters and space'}),
            # "PAN_No": forms.TextInput(attrs={"class": "form-control ", 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Pan number does not contain special charecters and space'}),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Company_Name", css_class="col-md-4 pe-0"),
            Column("Company_Address", css_class="col-md-8 "),
            Column("Company_City", css_class="col-md-3 pe-0 my-2 "),
            Column("Company_State", css_class="col-md-3 pe-0 my-2 "),
            Column("Company_Zip", css_class="col-md-3 pe-0 my-2 "),
            Column("Company_Country", css_class="col-md-3 my-2 "),
            Column("Founder_Name", css_class="col-md-3 pe-0"),
            Column("Founder_Email", css_class="col-md-3 pe-0"),
            Column("Founder_Address", css_class="col-md-6 "),
            Column("Founder_City", css_class="col-md-3 my-2 pe-0"),
            Column("Founder_State", css_class="col-md-3 my-2 pe-0"),
            Column("Founder_Zip", css_class="col-md-3 my-2 pe-0"),
            Column("Founder_Country", css_class="col-md-3 my-2"),
            Column("delivery_Address", css_class="col-md-4 pe-0"),
            Column("delivery_City", css_class="col-md-2 pe-0"),
            Column("delivery_State", css_class="col-md-2 pe-0"),
            Column("delivery_Zip", css_class="col-md-2 pe-0"),
            Column("delivery_Country", css_class="col-md-2"),
            Column("GST_Type", css_class="col-md-2 pe-0 mt-2"),
            Column("No_Of_Project", css_class="col-md-2 pe-0 mt-2"),
            Column("Payment_Terms", css_class="col-md-2  pe-0 mt-2"),
            Column("Company_Email", css_class="col-md-6 d-none"),
            Column("Company_Logo", css_class="col-md-6 d-none"),
            Column("Founder_Phone", css_class="col-md-6 d-none"),
            Column("Customer_Staff_Account", css_class="col-md-6 d-none"),
            Column("Bank_Account", css_class="col-md-6 d-none"),
            Column("Branches", css_class="col-md-6 d-none"),
            Column("TIN_No", css_class="col-md-6 d-none"),
            Column("GST_No", css_class="col-md-6 d-none"),
            Column("PAN_No", css_class="col-md-6 d-none"),
            Column("Certificate", css_class="col-md-6 d-none"),
            Column("User", css_class="col-md-12 mt-2"),
            Column("is_active", css_class="col-md-12 mt-2 d-none"),
            css_class="form-row row",
        ),
        FormActions(
            Submit("add_customer", "Add Customer", css_class="mt-2  btn-sm"),
            css_class="form-row add_agencies",
        ),
    )


class CustomerStaffForm(forms.ModelForm):
    class Meta:
        model = models.CustomerStaff
        fields = "__all__"

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Name", css_class="col-md-2 mb-1 "),
            Column("Contact_No", css_class="col-md-2 px-0"),
            Column("Email", css_class="col-md-2 pe-0"),
            Column("Position", css_class="col-md-3 "),
            Column("Location", css_class="col-md-3 ps-0"),
            Column("City", css_class="col-md-2 mt-1 "),
            Column("Zip", css_class="col-md-2 mt-1 px-0"),
            Column("State", css_class="col-md-2 mt-1 pe-0"),
            Column("Country", css_class="col-md-3 mt-1 px-3"),
            Column(
                FormActions(
                    Submit(
                        "add_customerstaffdetail",
                        "Add Customer Staff Detail",
                        css_class="mt-4  btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )

    def clean(self):
        return super().clean()


class CustomerDeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = models.CustomerDeliveryAddress
        fields = "__all__"

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Customer_Name", css_class="col-md-3 pe-0"),
            Column("Branch", css_class="col-md-3 pe-0"),
            Column("URL_Location_Of_The_Unloading_Place", css_class="col-md-3 pe-0"),
            Column("URL_Office_Location", css_class="col-md-3"),
            Column("URL_Of_Owner_House", css_class="col-md-3 pe-0"),
            Column("Invoice_Submitting_URL", css_class="col-md-3 pe-0 "),
            Column("Payment_Collecting_URL", css_class="col-md-3 pe-0 "),
            Column("Add_other_URL", css_class="col-md-3 "),
            Column(
                FormActions(
                    Submit(
                        "add_customerdeliveryaddress",
                        "Add Customer Delivery Address",
                        css_class="mt-2  btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )


class CustomerGSTBillingAddressForm(forms.ModelForm):
    class Meta:
        model = models.CustomerGSTBillingAddress
        fields = "__all__"
        widgets = {
            "Scan_Copy": forms.FileInput(
                attrs={
                    "class": "form-control ",
                    "required": False,
                }
            ),
            "Photo": forms.FileInput(
                attrs={
                    "class": "form-control ",
                    "required": False,
                }
            ),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("GST_No", css_class="col-md-6 pe-2"),
            Column("Scan_Copy", css_class="col-md-6 ps-2"),
            Column("Address", css_class="col-md-12 mt-0"),
            Column("City", css_class="col-md-3 pe-0 mt-1"),
            Column("Zip", css_class="col-md-2 pe-0 mt-1"),
            Column("State", css_class="col-md-4 pe-0 mt-1"),
            Column("Country", css_class="col-md-3 mt-1"),
            Column("Location_Url", css_class="col-md-4 pe-0 mt-1"),
            Column("Mobile", css_class="col-md-4 pe-0 mt-1"),
            Column("Mail_Id", css_class="col-md-4  mt-1"),
            Column("Photo", css_class="col-md-12 mt-1"),
            Column(
                FormActions(
                    Submit(
                        "add_customergstbillingaddress",
                        "Add Customer GST Billing Address",
                        css_class="mt-0 btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )


class CustomerBankAccountsForm(forms.ModelForm):
    class Meta:
        model = models.CustomerBankAccounts
        fields = "__all__"

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Customer_Name", css_class="col-md-12 "),
            Column("Category", css_class="col-md-6 pe-2 mt-1"),
            Column("Account_No", css_class="col-md-6 ps-2 mt-1"),
            Column("IFSC_Code", css_class="col-md-4 mt-1 pe-0"),
            Column("Branch", css_class="col-md-3 pe-0 mt-1"),
            Column("Register_Phone", css_class="col-md-5  mt-1"),
            Column(
                FormActions(
                    Submit(
                        "add_customerbankaccounts",
                        "Add Customer Bank Accounts",
                        css_class="mt-2 btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )
