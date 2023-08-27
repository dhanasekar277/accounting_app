from django.core import validators
from django import forms
from django.db.models import fields
from django.db.models.fields.files import FileField
from django.forms import widgets
from apps.vendors import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import FormActions


class VendorForm(forms.ModelForm):
    class Meta:
        model = models.Vendor
        fields = "__all__"
        widgets = {
            "User": forms.TextInput(
                attrs={"class": "form-control ", "value": "", "type": "hidden"}
            ),
            "Vendor_Name": forms.TextInput(attrs={"class": "form-control ",'required': True, 'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            "Company_Name": forms.TextInput(attrs={"class": "form-control ",'required': True}),
            "Phone": forms.TextInput(attrs={"class": "form-control ", 'required': True,'pattern':'^\d{10}$', 'title':'Enter your valid 10 digit mobile number'}),
            "Email": forms.TextInput(attrs={"class": "form-control ", 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
            'City': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'City contains alphabets only'}),
            'Zip': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^\d{6}$', 'title':'Zip contains six numbers only'}),
            'State': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'State contains alphabets only'}),
            'Country': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'Country contains alphabets only'}),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Vendor_Type", css_class="col-md-3 pe-0"),
            Column("Agency", css_class="col-md-3 pe-0 agency_select d-none"),
            Column("Vendor_Name", css_class="col-md-3 pe-0"),
            Column("Company_Name", css_class="col-md-3 pe-0"),
            Column("Vendor_Category", css_class="col-md-3", data_name="multiple"),
            Column("Phone", css_class="col-md-3 mt-2 mb-1 pe-0"),
            Column("Email", css_class="col-md-3 mt-2 mb-1 pe-0"),
            Column("Photo", css_class="col-md-3 mt-2 mb-1 pe-0"),
            Column("No_Of_Trucks", css_class="col-md-1 mt-2 mb-1 pe-0"),
            Column("Payment_Capabilities", css_class="col-md-2 mt-2 mb-1"),
            Column("Address", css_class="col-md-5 pe-0 "),
            Column("City", css_class="col-md-2 pe-0 "),
            Column("Zip", css_class="col-md-1 pe-0 "),
            Column("State", css_class="col-md-2 pe-0 "),
            Column("Country", css_class="col-md-2  "),
            Column("Agency", css_class="col-md-4  mt-2 d-none"),
            Column("GST_No", css_class="col-md-4 px-0 mt-2 d-none"),
            Column("Vendor_Staff_Detail", css_class="col-md-4 mt-2 d-none"),
            Column("Material_Supplying", css_class="col-md-4 mt-2 d-none"),
            Column("Material_From", css_class="col-md-4 mt-2 d-none"),
            Column("Material_To", css_class="col-md-4 mt-2 d-none"),
            Column("TIN_No", css_class="col-md-4 mt-2 d-none"),
            Column("PAN_No", css_class="col-md-4 mt-2 d-none"),
            Column("Certificate", css_class="col-md-4 mt-2 d-none"),
            Column("User", css_class="col-md-12 mt-2"),
            Column("is_active", css_class="col-md-12 mt-2 d-none"),
            css_class="form-row row",
        ),
        FormActions(
            Submit("add_vendor", "Add Vendor", css_class="mt-2  btn-sm"),
            css_class="form-row add_agencies",
        ),
    )


class VendorStaffDetailForm(forms.ModelForm):
    class Meta:
        model = models.VendorStaffDetail
        fields = "__all__"
        widgets = {
            "Vendor_Company_Name": forms.TextInput(attrs={"class": "form-control ",'required': True, 'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            "Account_Name": forms.TextInput(attrs={"class": "form-control ",'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            "Mobile": forms.TextInput(attrs={"class": "form-control ", 'required': True,'pattern':'^\d{10}$', 'title':'Enter your valid 10 digit mobile number'}),
            "Payment_Mobile": forms.TextInput(attrs={"class": "form-control ", 'required': True,'pattern':'^\d{10}$', 'title':'Enter your valid 10 digit mobile number'}),
            "Mail_Id": forms.TextInput(attrs={"class": "form-control ", 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
            "Payment_Mail_Id": forms.TextInput(attrs={"class": "form-control ", 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
            "Address": forms.Textarea(attrs={"class": "form-control ", "rows": "1"}),
            "Payment_Address": forms.Textarea(attrs={"class": "form-control ", "rows": "1"}),
            "Driver_Details": forms.Textarea(attrs={"class": "form-control ", "rows": "1"}),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Vendor_Company_Name", css_class="col-md-3 mb-1 "),
            Column("Account_Name", css_class="col-md-3 px-0"),
            Column("Mobile", css_class="col-md-3 pe-0"),
            Column("Mail_Id", css_class="col-md-3 "),
            Column("Address", css_class="col-md-12"),
            Column("Payment_Name", css_class="col-md-4 mt-2 "),
            Column("Payment_Mobile", css_class="col-md-4 mt-2 px-0"),
            Column("Payment_Mail_Id", css_class="col-md-4 mt-2 "),
            Column("Payment_Address", css_class="col-md-6 mt-2 pe-2"),
            Column("Driver_Details", css_class="col-md-6 mt-2 ps-2"),
            Column(
                FormActions(
                    Submit(
                        "add_vendorstaffdetail",
                        "Add Staff Detail",
                        css_class="mt-2  btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )


class VendorGSTForm(forms.ModelForm):
    class Meta:
        model = models.VendorGST
        fields = "__all__"
        widgets = {
            "Vendor_Company_Name": forms.TextInput(attrs={"class": "form-control ",'required': True, 'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            "Vendor_GST_No": forms.TextInput(attrs={"class": "form-control ", 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Gst number does not contain special charecters and space'}),
            "Vendor_PAN_No": forms.TextInput(attrs={"class": "form-control ", 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Pan number does not contain special charecters and space'}),
            "Vendor_Tin": forms.TextInput(attrs={"class": "form-control ", 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Tin number does not contain special charecters and space'}),
            "Vendor_Phone_Number": forms.TextInput(attrs={"class": "form-control ", 'required': True,'pattern':'^\d{10}$', 'title':'Enter your valid 10 digit mobile number'}),
            "Vendor_Email": forms.TextInput(attrs={"class": "form-control ", 'required': True, 'pattern':"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'title':'Please enter valid email address'}),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Vendor_Company_Name", css_class="col-md-3 pe-0"),
            Column("Vendor_GST_Type", css_class="col-md-3 pe-0"),
            Column("Vendor_GST_No", css_class="col-md-3 pe-0"),
            Column("Vendor_PAN_No", css_class="col-md-3 "),
            Column("Vendor_Bank_Account", css_class="col-md-6 pe-2 my-2"),
            Column("Vendor_Certificate", css_class="col-md-6 ps-2 my-2"),
            Column("Vendor_Phone_Number", css_class="col-md-4 "),
            Column("Vendor_Email", css_class="col-md-4 px-0"),
            Column("Vendor_Tin", css_class="col-md-4"),
            Column(
                FormActions(
                    Submit("add_vendorgst", "Add Vendor GST", css_class="mt-2  btn-sm")
                )
            ),
            css_class="form-row row",
        ),
    )


class VendorCertificateForm(forms.ModelForm):
    class Meta:
        model = models.VendorCertificate
        fields = "__all__"
        widgets = {
            "Vendor_Certificate_Scan_Copy": forms.FileInput(
                attrs={
                    "class": "form-control ",
                    "required": False,
                }
            ),
            "Vendor_Company_Name": forms.TextInput(attrs={"class": "form-control ",'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            "Vendor_Certificate_Name": forms.TextInput(attrs={"class": "form-control ", 'pattern':"^[a-zA-Z0-9_.-]*$", 'title':'Certificate number does not contain special charecters and space'}),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Vendor_Company_Name", css_class="col-md-6 pe-2"),
            Column("Vendor_Certificate_Name", css_class="col-md-6 ps-2"),
            Column("Vendor_Certificate_Scan_Copy", css_class="col-md-12 ps-2 mt-2"),
            Column(
                FormActions(
                    Submit(
                        "add_vendorcertificate",
                        "Add Vendor Certificate",
                        css_class="mt-0 btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )


class VendorGSTBankAccountForm(forms.ModelForm):
    class Meta:
        model = models.VendorGSTBankAccount
        fields = "__all__"
        widgets = {
            "Vendor_Company_Name": forms.TextInput(attrs={"class": "form-control ",'required': True, 'pattern':'^[A-Za-z_ ]+', 'title':'Name contains alphabets only'}),
            'City': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'City contains alphabets only'}),
            'Zip': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^\d{6}$', 'title':'Zip contains six numbers only'}),
            'State': forms.TextInput(attrs={'class':'form-control ', 'pattern':'^[A-Za-z_ ]+', 'title':'State contains alphabets only'}),
        }

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("Vendor_Company_Name", css_class="col-md-6 pe-2"),
            Column("Address", css_class="col-md-6 ps-2"),
            Column("City", css_class="col-md-5 mt-2 pe-2"),
            Column("Zip", css_class="col-md-2 px-2 mt-2"),
            Column("State", css_class="col-md-5  mt-2"),
            Column(
                FormActions(
                    Submit(
                        "add_vendorgstbankaccount",
                        "Add Vendor GST Bank Account",
                        css_class="mt-2 btn-sm",
                    )
                )
            ),
            css_class="form-row row",
        ),
    )
