from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest import serializers
from rest_framework.authentication import TokenAuthentication
from apps.agency.models import Agency, AgencyBankAccount, AgencyCertificate, AgencyPhone, Signature
from apps.vendors.models import Vendor, VendorGST, VendorStaffDetail, Material_From, Material_To, Sub_Location, MaterialQuality, Material_Supplying
from apps.products.models import Product, ProductQuality, LatestPrice
from apps.customers.models import Customer,Branch, CustomerDeliveryAddress,BranchDeliveryAddres, CustomerStaff, CustomerBankAccounts, CustomerGSTBillingAddress, PANNo, TINNo, CustomerCertifcate, CustomerPhoneNumber
from apps.orders.models import MaterialOrder, Order, PONumber, POMaterialInfo
from apps.home.models import Notification, Attendance
from apps.quicknotes.models import Quicknotes
from apps.bankentries.models import BankEntry
from apps.quotations.models import Quotation, SalesQuotation, PurchaseQuotation, VendorQuotationDetail, CustomerQuotationTerms, CustomerQuotationDetail
from apps.voucher.models import PurchaseInfo, VourchersAmount, VoucherDetail, VoucherSignature, VoucherVendorInfo, Voucher
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from apps.purchase.models import PurchaseMaterialEntry, PurchaseRemainder, PurchaseNetAmount, SinglePurchaseEntry, PurchaseEntry, purchaseInvoice
from apps.sales.models import CustomerInfo, SalesMaterialInfo, Sales, Total, SalesCollection
from apps.invoice.models import SalesInvoice, SingleSalesInvoice, DCDetail
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.loan.models import Loan, Repayment
from apps.bankentries.models import BankEntry
from apps.expences.models import Expences,ExpenceCategories,Assets


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = serializers.UserSerializere
    permission_classes = [permissions.IsAuthenticated]

class AgencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint  
    """
    queryset = Agency.objects.all().order_by('-id')
    serializer_class = serializers.AgencySerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,) 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Active']

""" Signature API Call """
class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all().order_by('-id')
    serializer_class = serializers.SignatureSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AgencyPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint  
    """
    queryset = Agency.objects.all().order_by('-id')
    serializer_class = serializers.PostAgencySerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Agency Bank API endpoint   """
class AgencyBankAccountViewSet(viewsets.ModelViewSet):
    queryset = AgencyBankAccount.objects.all().order_by('-id')
    serializer_class = serializers.AgencyBankAccountSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Agency Bank API endpoint   """
class AgencyPhoneViewSet(viewsets.ModelViewSet):
    queryset = AgencyPhone.objects.all().order_by('-id')
    serializer_class = serializers.AgencyPhoneSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Agency Certificates API endpoint   """
class AgencyCertificateViewSet(viewsets.ModelViewSet):
    queryset = AgencyCertificate.objects.all().order_by('-id')
    serializer_class = serializers.AgencyCertificateSerializer
    # permission_classes = [permissions.IsAuthenticated]

 
""" Vendor Staff Detail. """
class VendorStaffViewSet(viewsets.ModelViewSet):
    queryset = VendorStaffDetail.objects.all().order_by('-id')
    serializer_class = serializers.VendorStaffDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Vendor Material From Serializer Detail. """
class VendorMaterialFromViewSet(viewsets.ModelViewSet):
    queryset = Material_From.objects.all().order_by('-id')
    serializer_class = serializers.VendorMaterialFromSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Vendor Sub location Serializer Detail. """
class VendorSubLocationViewSet(viewsets.ModelViewSet):
    queryset = Sub_Location.objects.all().order_by('-id')
    serializer_class = serializers.VendorSubLocationSerializer
    # permission_classes = [permissions.IsAuthenticated]


"""Vendor GST Serializer"""
class POSTVendorGSTViewSet(viewsets.ModelViewSet):
    queryset = VendorGST.objects.all().order_by('-id')
    serializer_class = serializers.POSTVendorGSTSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Vendor Sub location Serializer Detail. """
class VendorMaterialQualityViewSet(viewsets.ModelViewSet):
    queryset = MaterialQuality.objects.all().order_by('-id')
    serializer_class = serializers.VendorMaterialQualitySerializer
    # permission_classes = [permissions.IsAuthenticated]



""" Vendor Material To Serializer Detail. """
class VendorMaterialToViewSet(viewsets.ModelViewSet):
    queryset = Material_To.objects.all().order_by('-id')
    serializer_class = serializers.VendorMaterialToSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Vendor Material Supplying Serializer Detail. """
class VendorMaterialSupplyingViewSet(viewsets.ModelViewSet):
    queryset = Material_Supplying.objects.all().order_by('-id')
    serializer_class = serializers.VendorMaterialSupplyingSerializer
    # permission_classes = [permissions.IsAuthenticated]
""" Post Vendor Material Supplying Serializer Detail. """
class PostVendorMaterialSupplyingViewSet(viewsets.ModelViewSet):
    queryset = Material_Supplying.objects.all().order_by('-id')
    serializer_class = serializers.PostVendorMaterialSupplyingSerializer

""" Vendor API endpoint   """
class VendorsViewSet(viewsets.ModelViewSet):

    queryset = Vendor.objects.all().order_by('-id')
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = serializers.Result_20_Pagination



""" Post Vendor API endpoint   """
class VendorPostViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('-id')
    serializer_class = serializers.POSTVendorSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Product Quality API endpoint   """
class ProductQualityViewSet(viewsets.ModelViewSet):
    queryset = ProductQuality.objects.all().order_by('-id')
    serializer_class = serializers.ProductQualitySerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Latest Price API endpoint   """
class LatestPriceViewSet(viewsets.ModelViewSet):
    queryset = LatestPrice.objects.all().order_by('-id')
    serializer_class = serializers.LatestPriceSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint  
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = serializers.ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Product', 'Vendor']


class ProductWithOutViewSet(viewsets.ModelViewSet):
    """
    API endpoint  
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = serializers.ProductSerializerWithOutInfo
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Product']


""" Customer Staff API endpoint   """
class CustomerStaffViewSet(viewsets.ModelViewSet):
    queryset = CustomerStaff.objects.all().order_by('-id')
    serializer_class = serializers.CustomerStaffSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer Staff API endpoint   """
class CustomerBranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('-id')
    serializer_class = serializers.CustomerBranchSerializer
    # permission_classes = [permissions.IsAuthenticated]



""" Customer Delivery Address API endpoint  """
class CustomerDeliverAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerDeliveryAddress.objects.all().order_by('-id')
    serializer_class = serializers.CustomerDeliveryAddressSerializer
    # permission_classes = [permissions.IsAuthenticated]



"""  Customer Branch Delivery Addres Serializers API endpoint  """
class CustomerBranchDeliveryAddresViewSet(viewsets.ModelViewSet):
    queryset = BranchDeliveryAddres.objects.all().order_by('-id')
    serializer_class = serializers.CustomerBranchDeliveryAddresSerializers
    # permission_classes = [permissions.IsAuthenticated]


""" Customer Post API endpoint   """
class CustomerPostViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = serializers.POSTCustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer Bank Account API endpoint   """
class CustomerBankAccountViewSet(viewsets.ModelViewSet):
    queryset = CustomerBankAccounts.objects.all().order_by('-id')
    serializer_class = serializers.CustomerBankAccountSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer Bank Account API endpoint   """
class CustomerGSTBillingAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerGSTBillingAddress.objects.all().order_by('-id')
    serializer_class = serializers.CustomerGSTBillingSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer PAN No API endpoint   """
class CustomerPANNoViewSet(viewsets.ModelViewSet):
    queryset = PANNo.objects.all().order_by('-id')
    serializer_class = serializers.PANNoSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer Certifcate API endpoint   """
class CustomerCertifcateViewSet(viewsets.ModelViewSet):
    queryset = CustomerCertifcate.objects.all().order_by('-id')
    serializer_class = serializers.CustomerCertifcateSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer TIN No API endpoint  """
class CustomerTINNoViewSet(viewsets.ModelViewSet):
    queryset = TINNo.objects.all().order_by('-id')
    serializer_class = serializers.TINNoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    
""" Customer API endpoint   """
class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = serializers.CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,) 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Company_Name']
    pagination_class = serializers.Result_20_Pagination


""" Order API endpoint """
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = serializers.OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Order Post API endpoint  """
class POSTOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = serializers.POSTOrderSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Material Info API endpoint """
class MaterialInfo_ViewSet(viewsets.ModelViewSet):
    queryset = MaterialOrder.objects.all().order_by('-id')
    serializer_class = serializers.MaterialInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MaterialInfoWithInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint  
    """
    queryset = MaterialOrder.objects.all().order_by('-id')
    serializer_class = serializers.MaterialInfoSerializerWithInfo
    # permission_classes = [permissions.IsAuthenticated]

 
class POMaterialInfoViewSet(viewsets.ModelViewSet):
    queryset = POMaterialInfo.objects.all().order_by('-id')
    serializer_class = serializers.POMaterialInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class POViewSet(viewsets.ModelViewSet):
    queryset = PONumber.objects.all().order_by('-id')
    serializer_class = serializers.PONumberSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Purchase Quotation API endpoint """
class PurchaseQuotationViewSet(viewsets.ModelViewSet):
    queryset = PurchaseQuotation.objects.all().order_by('-id')
    serializer_class = serializers.PurchaseQuotationSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Sales Quotation API endpoint """
class SalesQuotationViewSet(viewsets.ModelViewSet):
    queryset = SalesQuotation.objects.all().order_by('-id')
    serializer_class = serializers.SalesQuotationSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Customer Quotation Detail API endpoint """
class CusQuotationDetailViewSet(viewsets.ModelViewSet):
    queryset = CustomerQuotationDetail.objects.all().order_by('-id')
    serializer_class = serializers.CusQuotationDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]

    
""" Customer Quotation Term API endpoint """
class CusQuotationTermsViewSet(viewsets.ModelViewSet):
    queryset = CustomerQuotationTerms.objects.all().order_by('-id')
    serializer_class = serializers.CusQuotationTermSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Vendor Quotation Detail API endpoint """
class GenVendorQuotationDetailViewSet(viewsets.ModelViewSet):
    queryset = VendorQuotationDetail.objects.all().order_by('-id')
    serializer_class = serializers.GetVenQuotationDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Vendor Quotation Detail API endpoint """
class VendorQuotationDetailViewSet(viewsets.ModelViewSet):
    queryset = VendorQuotationDetail.objects.all().order_by('-id')
    serializer_class = serializers.VenQuotationDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Quotation API endpoint """
class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all().order_by('-id')
    serializer_class = serializers.QuotationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']


""" Get Quotation API endpoint """
class GetQuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all().order_by('-id')
    serializer_class = serializers.GetQuotationSerializer
    # permission_classes = [permissions.IsAuthenticated]


"""Notification start here"""
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-id')
    serializer_class = serializers.NotificationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    

"""Notification start here"""
class NotificationWithOutInfoViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-id')
    serializer_class = serializers.NotificationWithOutSerializer
    # permission_classes = [permissions.IsAuthenticated]



"""Attendacne start here"""
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by('-id')
    serializer_class = serializers.AttendanceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Punch_Out_Time']


"""Wuick Notes start here"""
class QuickNotesViewSet(viewsets.ModelViewSet):
    queryset = Quicknotes.objects.all().order_by('-id')
    serializer_class = serializers.QuickNotesSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Purchase entry view set """
class PostPurchaseMaterialEntryViewSet(viewsets.ModelViewSet):
    queryset = PurchaseMaterialEntry.objects.all().order_by('-id')
    serializer_class = serializers.PostPurchaseMaterialEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['p_id'] 


""" Purchase Remainder view set """
class PostPurchaseRemainderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRemainder.objects.all().order_by('-id')
    serializer_class = serializers.PostPurchaseRemainderSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Purchase Net Amount ViewSet """
class PostPurchaseNetAmountViewSet(viewsets.ModelViewSet):
    queryset = PurchaseNetAmount.objects.all().order_by('-id')
    serializer_class = serializers.PostPurchaseNetAmountSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Post Single Purchase Entry View Set """
class PostSinglePurchaseEntryViewSet(viewsets.ModelViewSet):
    queryset = SinglePurchaseEntry.objects.all().order_by('-id')
    serializer_class = serializers.PostSinglePurchaseEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quotation', 'vendorId', 'purchaseMaterial']

""" Post Purchase Entry ViewSet """
class PostPurchaseEntryViewSet(viewsets.ModelViewSet):
    queryset = PurchaseEntry.objects.all().order_by('-id')
    serializer_class = serializers.PostPurchaseEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quotation', 'vendorId']

""" Get Purchase entry view set """
class GetPurchaseMaterialEntryViewSet(viewsets.ModelViewSet):
    queryset = PurchaseMaterialEntry.objects.all().order_by('-id')
    serializer_class = serializers.GetPurchaseMaterialEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Get Purchase Remainder view set """
class GetPurchaseRemainderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRemainder.objects.all().order_by('-id')
    serializer_class = serializers.GetPurchaseRemainderSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Get Purchase Net Amount ViewSet """
class GetPurchaseNetAmountViewSet(viewsets.ModelViewSet):
    queryset = PurchaseNetAmount.objects.all().order_by('-id')
    serializer_class = serializers.GetPurchaseNetAmountSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostPurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = purchaseInvoice.objects.all().order_by('-id')
    serializer_class = serializers.PostPurchaseInvoiceSerialzer
    # permission_classes = [permissions.IsAuthenticated]


""" Get Single Purchase Entry View Set """
class GetSinglePurchaseEntryViewSet(viewsets.ModelViewSet):
    queryset = SinglePurchaseEntry.objects.all().order_by('-id')
    serializer_class = serializers.GetSinglePurchaseEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Get Purchase Entry ViewSet """
class GetPurchaseEntryViewSet(viewsets.ModelViewSet):
    queryset = PurchaseEntry.objects.all().order_by('-id')
    serializer_class = serializers.GetPurchaseEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quotation']

""" Get Voucher Signature ViewSet """
class GetVoucherSignatureViewSet(viewsets.ModelViewSet):
    queryset = VoucherSignature.objects.all().order_by('-id')
    serializer_class = serializers.GetVoucherSignatureSerializer
    # permission_classes = [permissions.IsAuthenticated]

# PurchaseBasicInfo, VoucherPurchase, VourcherAmount, Voucher
""" Voucher Detail Started """

class PostVoucherVendorInfoViewSet(viewsets.ModelViewSet):
    queryset = VoucherVendorInfo.objects.all().order_by('-id')
    serializer_class = serializers.PostVoucherVendorInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Post Purchase Basic Info ViewSet """
class PostPurchaseBasicInfoViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInfo.objects.all().order_by('-id')
    serializer_class = serializers.PostPurchaseBasicInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Post Voucher Purchase ViewSet """
class PostVourcherAmountViewSet(viewsets.ModelViewSet):
    queryset = VourchersAmount.objects.all().order_by('-id')
    serializer_class = serializers.PostVourcherAmountSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Post Voucher Purchase ViewSet """
class PostSingleVoucherViewSet(viewsets.ModelViewSet):
    queryset = VoucherDetail.objects.all().order_by('-id')
    serializer_class = serializers.PostSingleVoucherSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Post Voucher Signature ViewSet """
class PostVoucherSignatureViewSet(viewsets.ModelViewSet):
    queryset = VoucherSignature.objects.all().order_by('-id')
    serializer_class = serializers.PostVoucherSignatureSerializer
    # permission_classes = [permissions.IsAuthenticated]
 
""" Get voucher Entry ViewSet """
class GetVoucherViewSet(viewsets.ModelViewSet):
    queryset = VoucherDetail.objects.all().order_by('-id')
    serializer_class = serializers.GetVoucherSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quotation', 'VendorId']
 

class VouchersViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all().order_by('-id')
    serializer_class = serializers.VoucherSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quotation']


class PostVouchersViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all().order_by('-id')
    serializer_class = serializers.PostVoucherSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quotation']





""" Sales Entry ViewSet """
""" Get Total ViewSet """

""" Get CustomerInfo ViewSet """
class GetCutomerInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all().order_by('-id')
    serializer_class = serializers.GetCustomerInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Post CustomerInfo ViewSet """
class PostCutomerInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all().order_by('-id')
    serializer_class = serializers.PostCustomerInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Get SalesMaterialInfo Serializer ViewSet """
class GetSalesMaterialInfoViewSet(viewsets.ModelViewSet):
    queryset = SalesMaterialInfo.objects.all().order_by('-id')
    serializer_class = serializers.GetSalesMaterialInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['orderId']
    pagination_class = serializers.Result_50_Pagination


""" Get SalesMaterialInfo Serializer ViewSet """
class PostSalesMaterialInfoViewSet(viewsets.ModelViewSet):
    queryset = SalesMaterialInfo.objects.all().order_by('-id')
    serializer_class = serializers.PostSalesMaterialInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Get Sales ViewSet """
class GetSalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all().order_by('-id')
    serializer_class = serializers.GetSalesSerializer
    # permission_classes = [permissions.IsAuthenticated]

class PostSalesTotalViewSet(viewsets.ModelViewSet):
    queryset = Total.objects.all().order_by('-id')
    serializer_class = serializers.PostTotalSerializer
    # permission_classes = [permissions.IsAuthenticated]

""" Post Sales ViewSet """
class PostSalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all().order_by('-id')
    serializer_class = serializers.PostSalesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostSalesCollectionViewSet(viewsets.ModelViewSet):
    queryset = SalesCollection.objects.all().order_by('-id')
    serializer_class = serializers.PostSaleCollectionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['orderid']

""" Customer Phone Number ViewSet """
class CustomerPhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = CustomerPhoneNumber.objects.all().order_by('-id')
    serializer_class = serializers.CustomerPhoneNumberSerializer
    # permission_classes = [permissions.IsAuthenticated]


""" Sales Invoice Viewset starts here"""
"""  Get DCDetail ViewSet """
# SalesInvoice, SingleSalesInvoice, DCDetail
class GetDCDetailViewSet(viewsets.ModelViewSet):
    queryset = DCDetail.objects.all().order_by('-id')
    serializer_class = serializers.GetDCDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['poid']

"""  Get Single Sales Invoice ViewSet """
class GetSingleSalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SingleSalesInvoice.objects.all().order_by('-id')
    serializer_class = serializers.GetSingleSalesInvoiceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['saleid']

"""  Get Sales Invoice ViewSet """
class GetSalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all().order_by('-id')
    serializer_class = serializers.GetSalesInvoiceSerializer
    # permission_classes = [permissions.IsAuthenticated]
"""  Post DCDetail ViewSet """
class PostDCDetailViewSet(viewsets.ModelViewSet):
    queryset = DCDetail.objects.all().order_by('-id')
    serializer_class = serializers.PostDCDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]


"""  Post Single Sales Invoice ViewSet """
class PostSingleSalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SingleSalesInvoice.objects.all().order_by('-id')
    serializer_class = serializers.PostSingleSalesInvoiceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['saleid']

"""  Post Sales Invoice ViewSet """
class PostSalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all().order_by('-id')
    serializer_class = serializers.PostSalesInvoiceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['saleid']


class PostBankEntryViewSet(viewsets.ModelViewSet):
    queryset = BankEntry.objects.all().order_by('-id')
    serializer_class = serializers.postBankEntrySerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['voucherId']
    
"""Loan Management start here"""
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by('-id')
    serializer_class = serializers.LoanSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RepaymentViewSet(viewsets.ModelViewSet):
    queryset = Repayment.objects.all().order_by('-id')
    serializer_class = serializers.RepaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


"""BankEntry Management start here"""
class BankEntryViewSet(viewsets.ModelViewSet):
    queryset = BankEntry.objects.all().order_by('-id')
    serializer_class = serializers.BankEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

"""Expences Management start here"""
class ExpencesViewSet(viewsets.ModelViewSet):
    queryset = Expences.objects.all().order_by('-id')
    serializer_class = serializers.ExpencesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExpenceCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ExpenceCategories.objects.all().order_by('-id')
    serializer_class = serializers.ExpenceCategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]

class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all().order_by('-id')
    serializer_class = serializers.AssetsSerializer
    permission_classes = [permissions.IsAuthenticated]


