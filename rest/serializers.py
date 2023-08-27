from django.contrib.auth.models import User, Group
from django.utils.regex_helper import Choice
from rest_framework import serializers
from apps.agency.models import Agency, AgencyBankAccount, AgencyCertificate, AgencyPhone, Signature
from apps.vendors.models import Vendor, VendorGST,VendorPAN, VendorStaffDetail,MaterialQuality, Material_Supplying, VendorGSTBankAccount, VendorCertificate, Material_From, Material_To, Sub_Location, GST_TYPE_CHOICES, VendorTIN
from apps.products.models import Product, ProductQuality, LatestPrice
from apps.customers.models import Customer,Branch, CustomerDeliveryAddress, CustomerStaff, CustomerCertifcate,PANNo, TINNo, CustomerGSTBillingAddress, CustomerBankAccounts, BranchDeliveryAddres, CustomerPhoneNumber
from apps.orders.models import  MaterialOrder, Order, PONumber, POMaterialInfo, QUANTITY_TYPE
from apps.home.models import Notification, Attendance, TYPE_CHOICES
from apps.quicknotes.models import Quicknotes
from apps.quotations.models import PurchaseQuotation, SalesQuotation, Quotation, VendorQuotationDetail, CustomerQuotationTerms, CustomerQuotationDetail
from apps.voucher.models import PurchaseInfo, VourchersAmount, VoucherDetail, VoucherSignature, VoucherVendorInfo, Voucher
from rest_framework.pagination import PageNumberPagination
from apps.purchase.models import PurchaseMaterialEntry, PurchaseRemainder, PurchaseNetAmount, SinglePurchaseEntry, PurchaseEntry, purchaseInvoice
from apps.sales.models import CustomerInfo, SalesMaterialInfo, Sales, Total, SalesCollection
from apps.invoice.models import SalesInvoice, SingleSalesInvoice, DCDetail
from apps.loan.models import Loan, Repayment
from apps.bankentries.models import BankEntry
from apps.expences.models import Expences,ExpenceCategories,Assets
# from django.contrib.auth import get_user_model


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class Result_20_Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class Result_50_Pagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50


# user serializers
class UserSerializere(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups','user_permissions','date_joined','last_login')

# SiteInfo,
class AgencyBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyBankAccount
        fields = '__all__'


class AgencyPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyPhone
        fields = '__all__'


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = '__all__'


class AgencyCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyCertificate
        fields = '__all__'


class PostAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'



class AgencySerializer(serializers.ModelSerializer):
    Bank_Account = AgencyBankAccountSerializer(many=True)
    Certificates = AgencyCertificateSerializer(many=True)
    Phone = AgencyPhoneSerializer(many=True)
    class Meta:
        model = Agency
        fields = '__all__'


class VendorMaterialFromSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material_From
        fields = '__all__'


class VendorSubLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Location
        fields = '__all__'

class GETVendorMaterialToSerializer(serializers.ModelSerializer):
    SubLocation = VendorSubLocationSerializer(many=True)
    class Meta:
        model = Material_To
        fields = '__all__'

class VendorMaterialToSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material_To
        fields = '__all__'


class VendorMaterialQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialQuality
        fields = '__all__'


# post
class PostVendorMaterialSupplyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material_Supplying
        fields = '__all__'
        
# get
class VendorMaterialSupplyingSerializer(serializers.ModelSerializer):
    Quality = VendorMaterialQualitySerializer(many=True)
    Material_From = VendorMaterialFromSerializer(many=True)
    Material_To = GETVendorMaterialToSerializer(many=True)

    class Meta:
        model = Material_Supplying
        fields = '__all__'


class VendorGSTBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorGSTBankAccount
        fields = '__all__'
 

class VendorCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorCertificate
        fields = '__all__'


class POSTVendorGSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorGST
        fields = '__all__'


class VendorGSTSerializer(serializers.ModelSerializer):
    Vendor_Certificate = VendorCertificateSerializer(many=True)
    Vendor_Bank_Account = VendorGSTBankAccountSerializer(many=True)
    class Meta:
        model = VendorGST
        fields = '__all__'


class VendorStaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorStaffDetail
        fields = '__all__'


class VendorPANSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPAN
        fields = '__all__'

class VendorTINSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorTIN
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    Material_Supplying = VendorMaterialSupplyingSerializer(many=True)
    # Material_From = VendorMaterialFromSerializer(many=True)
    # Material_To = GETVendorMaterialToSerializer(many=True)
    Vendor_Staff_Detail = VendorStaffDetailSerializer(many=True)
    Vendor_Type = ChoiceField(choices=GST_TYPE_CHOICES) 
    GST_No = POSTVendorGSTSerializer(many=True)
    PAN_No = VendorPANSerializer(many=True)
    TIN_No = VendorTINSerializer(many=True)
    class Meta:
        model = Vendor
        fields = '__all__'


class POSTVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'



class ProductQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuality
        fields = '__all__'
        

class LatestPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestPrice
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    Vendor = VendorSerializer()
    Quality = ProductQualitySerializer(many=True)
    LatestPrice = LatestPriceSerializer(many=True)
    Material_Supplying = VendorMaterialSupplyingSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        choices = validated_data.pop('Vendor')
        vendor = Vendor.objects.create(**validated_data)
        return vendor




class ProductSerializerWithOutInfo(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerCertifcateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCertifcate
        fields = '__all__'


class PANNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PANNo
        fields = '__all__'


class TINNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TINNo
        fields = '__all__'

class CustomerPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPhoneNumber
        fields = '__all__'

class CustomerBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CustomerBranchDeliveryAddresSerializers(serializers.ModelSerializer):
    class Meta:
        model = BranchDeliveryAddres
        fields = '__all__'


class CustomerDeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDeliveryAddress
        fields = '__all__'


class CustomerStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerStaff
        fields = '__all__'
 

class CustomerGSTBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGSTBillingAddress
        fields = '__all__'


class GetCustomerBranchSerializer(serializers.ModelSerializer):
    Billing_Address = CustomerGSTBillingSerializer()
    Delivery_Address = CustomerBranchDeliveryAddresSerializers(many=True)
    Staff_Detail= CustomerStaffSerializer(many=True)
    class Meta:
        model = Branch
        fields = '__all__'


class CustomerBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBankAccounts
        fields = '__all__'


class POSTCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    GST_No = CustomerGSTBillingSerializer(many=True)
    PAN_No = PANNoSerializer(many=True)
    TIN_No = TINNoSerializer(many=True)
    Branches = GetCustomerBranchSerializer(many=True)
    Customer_Staff_Account = CustomerStaffSerializer(many=True)
    Bank_Account = CustomerBankAccountSerializer(many=True)
    Founder_Phone = CustomerPhoneNumberSerializer(many=True)
    class Meta:
        model = Customer
        fields = '__all__'

class POMaterialInfoSerializer(serializers.ModelSerializer):
    Quantity_Type = ChoiceField(choices=QUANTITY_TYPE)
    class Meta:
        model = POMaterialInfo
        fields = '__all__'

class GetPOMaterialInfoSerializer(serializers.ModelSerializer):
    Quantity_Type = ChoiceField(choices=QUANTITY_TYPE)
    class Meta:
        model = POMaterialInfo
        fields = '__all__'

class MaterialInfoSerializer(serializers.ModelSerializer):
    Quantity_Type = ChoiceField(choices=QUANTITY_TYPE)
    class Meta:
        model = MaterialOrder
        fields = '__all__'

class MaterialInfoSerializerWithInfo(serializers.ModelSerializer):
    Vendor = VendorSerializer()
    Product_Name = ProductSerializerWithOutInfo()
    Mat_PO_ID = GetPOMaterialInfoSerializer()
    
    class Meta:
        model = MaterialOrder
        fields = '__all__'


class GetPONumberSerializer(serializers.ModelSerializer):
    PO_Material_Info = GetPOMaterialInfoSerializer(many=True)
    class Meta:
        model = PONumber
        fields = '__all__'

class PONumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PONumber
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    User = UserSerializere()
    Agency = AgencySerializer()
    PO_Number = GetPONumberSerializer()
    Materials = MaterialInfoSerializerWithInfo(many=True)
    Sales_Company = CustomerSerializer()
    class Meta:
        model = Order
        fields = '__all__'


class POSTOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


""" Purchase Quotation Start Here """
class PurchaseQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseQuotation
        fields = '__all__'  


""" Sales Quotation Start Here """
class SalesQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesQuotation
        fields = '__all__'  


class CusQuotationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuotationDetail
        fields = '__all__'


class CusQuotationTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuotationTerms
        fields = '__all__'


class GetVenQuotationDetailSerializer(serializers.ModelSerializer):
    mat_id = MaterialInfoSerializerWithInfo(many=True)
    class Meta:
        model = VendorQuotationDetail
        fields = '__all__'


class VenQuotationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorQuotationDetail
        fields = '__all__'

""" Quotation Start Here """
class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'  


""" Get Purchase Quotation Start Here """
class GetPurchaseQuotationSerializer(serializers.ModelSerializer):
    material = MaterialInfoSerializerWithInfo(many=True)
    class Meta:
        model = PurchaseQuotation
        fields = '__all__'  

 
""" Get Sales Quotation Start Here """
class GetSalesQuotationSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    po = PONumberSerializer()
    po_materials = GetPOMaterialInfoSerializer(many=True)

    class Meta:
        model = SalesQuotation
        fields = '__all__'  


""" Get Quotation Start Here """
class GetQuotationSerializer(serializers.ModelSerializer):
    purchase = GetPurchaseQuotationSerializer()
    sales = GetSalesQuotationSerializer()
    order = OrderSerializer()
    vendorInfo = VenQuotationDetailSerializer(many=True)
    customerInfo = CusQuotationTermSerializer()
    class Meta:
        model = Quotation
        fields = '__all__'  


# Notification start Here
class NotificationSerializer(serializers.ModelSerializer):
    Types = ChoiceField(choices=TYPE_CHOICES)
    User = UserSerializere()
    class Meta:
        model = Notification
        fields = '__all__'


# Notification start Here
class NotificationWithOutSerializer(serializers.ModelSerializer):
    Types = ChoiceField(choices=TYPE_CHOICES)
    class Meta:
        model = Notification
        fields = '__all__'
        
""" Attendance start here """
class AttendanceSerializer(serializers.ModelSerializer):
    User = UserSerializere()
    class Meta:
        model = Attendance
        fields = '__all__'

""" Quick Notes Start Here """
class QuickNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quicknotes
        fields = '__all__'    


""" Purchase Entry Section Starts Here """
""" Get Purchase Material Entry"""
class GetPurchaseMaterialEntrySerializer(serializers.ModelSerializer):
    mat_id = MaterialInfoSerializerWithInfo()
    class Meta:
        model = PurchaseMaterialEntry
        fields = '__all__'


""" Get Purchase Remainder Entry"""
class GetPurchaseRemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRemainder
        fields = '__all__'


""" Get Purchase Net Amount Entry"""
class GetPurchaseNetAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseNetAmount
        fields = '__all__'


class PostPurchaseInvoiceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = purchaseInvoice
        fields = '__all__'

""" Get Single Purchase Entry Entry"""
class GetSinglePurchaseEntrySerializer(serializers.ModelSerializer):
    vendorId = VendorSerializer()
    customerId = CustomerSerializer()
    purchaseMaterial = GetPurchaseMaterialEntrySerializer(many=True)
    remainder = GetPurchaseRemainderSerializer()
    netAmount = GetPurchaseNetAmountSerializer()
    quotation = GetQuotationSerializer()
    invoice = PostPurchaseInvoiceSerialzer()
    class Meta:
        model = SinglePurchaseEntry
        fields = '__all__'





""" Get Purchase Entry"""
class GetPurchaseEntrySerializer(serializers.ModelSerializer):
    entries = GetSinglePurchaseEntrySerializer(many=True)
    quotation = GetQuotationSerializer()
    class Meta:
        model = PurchaseEntry
        fields = '__all__'


class GetVoucherSignatureSerializer(serializers.ModelSerializer):
    signature_id = SignatureSerializer(many=True)
    class Meta:
        model = VoucherSignature
        fields = '__all__'


""" Post Purchase Material Entry"""
class PostPurchaseMaterialEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseMaterialEntry
        fields = '__all__'


""" Post Purchase Remainder Entry"""
class PostPurchaseRemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRemainder
        fields = '__all__'


""" Get Purchase Net Amount Entry"""
class PostPurchaseNetAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseNetAmount
        fields = '__all__'


""" Post Single Purchase Entry Entry"""
class PostSinglePurchaseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglePurchaseEntry
        fields = '__all__'


""" Post Purchase Entry"""
class PostPurchaseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseEntry
        fields = '__all__'


""" Voucher Section Started """
""" Post Purchase Basic Info Entry"""
class PostVoucherVendorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherVendorInfo
        fields = '__all__'

class PostPurchaseBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInfo
        fields = '__all__'

""" Post Vourcher Amount"""
class GetVourcherAmountSerializer(serializers.ModelSerializer):
    # GetPurchaseMaterialEntrySerializer
    VoucherMaterialInfo = PostPurchaseMaterialEntrySerializer(many=True)
    class Meta:
        model = VourchersAmount
        fields = '__all__'


class PostVourcherAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VourchersAmount
        fields = '__all__'

""" Post Vourcher """
class PostSingleVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherDetail
        fields = '__all__'

class PostVoucherSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherSignature
        fields = '__all__'


class PostVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'
 
""" Post Vourcher """
class GetVoucherSerializer(serializers.ModelSerializer):
    VendorId = VendorSerializer()
    amount = GetVourcherAmountSerializer(many=True)
    vendorDetail = PostVoucherVendorInfoSerializer()
    signature = PostVoucherSignatureSerializer(many=True)
    quotation = GetQuotationSerializer()
    class Meta:
        model = VoucherDetail
        fields = '__all__'


class VoucherSerializer(serializers.ModelSerializer):
    voucher = GetVoucherSerializer(many=True)
    class Meta:
        model = Voucher
        fields = '__all__'

""" Total, CustomerInfo, SalesMaterialInfo, Sales Info detail """
""" Total Serialize """

""" Get Customer Info Serializer """


class GetCustomerInfoSerializer(serializers.ModelSerializer):
    customerid = CustomerSerializer()
    phone = CustomerPhoneNumberSerializer()
    pan = PANNoSerializer()
    tin = TINNoSerializer()
    gst = CustomerGSTBillingSerializer()
    class Meta:
        model = CustomerInfo
        fields = '__all__'

class PostCustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'

class PostTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = '__all__'


# check this
""" Get Sales Material Info Serializer """
class GetSalesMaterialInfoSerializer(serializers.ModelSerializer):
    MatId = MaterialInfoSerializerWithInfo()
    class Meta:
        model = SalesMaterialInfo
        fields = '__all__'


""" Post Sales Material Info Serializer """
class PostSalesMaterialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesMaterialInfo
        fields = '__all__'


""" Get Sales Serializer """
class GetSalesSerializer(serializers.ModelSerializer):
    customer = GetCustomerInfoSerializer()
    orderid = OrderSerializer()
    poInfo = GetSalesMaterialInfoSerializer(many=True)
    remainder = GetPurchaseRemainderSerializer()
    netAmount = GetPurchaseNetAmountSerializer()
    class Meta:
        model = Sales
        fields = '__all__'


class PostSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class PostSaleCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesCollection
        fields = '__all__'


# SalesInvoice, SingleSalesInvoice, DCDetail
""" Get DCDetail erializer """
class GetDCDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DCDetail
        fields = '__all__'

""" Get Single Sales Invoice Serializer """
class GetSingleSalesInvoiceSerializer(serializers.ModelSerializer):
    DC = GetDCDetailSerializer(many=True)
    saleid = GetSalesSerializer()
    phone = AgencyPhoneSerializer()
    BankAccount = AgencyBankAccountSerializer()
    class Meta:
        model = SingleSalesInvoice
        fields = '__all__'

""" Get Sales Invoice Serializer """
class GetSalesCollectionSerializer(serializers.ModelSerializer):
    sales = GetSalesSerializer(many=True)
    class Meta:
        model = SalesCollection
        fields = '__all__'


""" Get Sales Invoice Serializer """
class GetSalesInvoiceSerializer(serializers.ModelSerializer):
    saleid = GetSalesCollectionSerializer()
    invoice = GetSingleSalesInvoiceSerializer(many=True)
    class Meta:
        model = SalesInvoice
        fields = '__all__'
""" Post DCDetail erializer """
class PostDCDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DCDetail
        fields = '__all__'
""" Post Single Sales Invoice Serializer """
class PostSingleSalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleSalesInvoice
        fields = '__all__'
""" Post Sales Invoice Serializer """
class PostSalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = '__all__'

""" Loan Mangaement Start Here """
class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = '__all__'   

class LoanSerializer(serializers.ModelSerializer):
    # Repayments = RepaymentSerializer(read_only=True, many=True)
    class Meta:
        model = Loan
        fields = '__all__'    


""" BankEntry Mangaement Start Here """
class postBankEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BankEntry
        fields = '__all__'

class BankEntrySerializer(serializers.ModelSerializer):
    InvoiceId = GetSingleSalesInvoiceSerializer()
    CustomerId = CustomerSerializer()
    class Meta:
        model = BankEntry
        fields = '__all__'


""" Expences Mangaement Start Here """
class ExpencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expences
        fields = '__all__'

class ExpenceCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenceCategories
        fields = '__all__'

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

