$(document).ready(function(){

    let rcategory 
    let rfrom 
    let rto 
    let page = 1
    // main search

    var agency_url = `${url}agency/?page=${page}`
    var vendor_url = `${url}vendors/?page=${page}`
    var customer_url = `${url}customers/?page=${page}`
    var product_url = `${url}products/?page=${page}`
    var order_url = `${url}orders/?page=${page}`
    var quotation_url = `${url}quotations/?page=${page}`
    var purchase_url = `${url}single-purchase-entry/?page=${page}`
    let voucher_url = `${url}voucher/?page=${page}`
    var sales_url = `${url}sales/?page=${page}`
    var invoice_url = `${url}single-invoice/?page=${page}`
    var api_data = []
    endof_api = false

    $('#report_search').click(function(e){
        e.preventDefault()

        var randid = randomClass()
        // console.log(randid)

        $('.reports thead tr, .reports tbody').html('')
        $('.fixTableHead').removeClass('d-none')

        var category = $('.reports #category').val()
        var from = $('.reports #from').val()
        var to = $('.reports #to').val()
        
        rcategory = category
        rfrom = from
        rto = to

        api_data = []

        if(category == 0){
            $('.fixTableHead').addClass('d-none')
            // select category
            alert('Select search category. !!!')
        }else{
            $('.no_results').addClass('d-none')
            // console.log(category)
            // select category
            GetCategoryData(category, 1)
        }

    })


    function GetCategoryData(category, page){

        if(category == 'agency'){
            // agency report function call
            agencyReport()
        }
        else if(category == 'vendor'){
            // vendor report function call
            vendorReport()
        }
        else if(category == 'customer'){
            // customer report function call
            customerReport()     
        }
        else if(category == 'product'){
            // product report function call
            productReport()
        }
        else if(category == 'order'){
            // order report function call
            ordereport()
        }
        else if(category == 'quotation'){
            // quotation report function call
            quotationReport(`${quotation_url}${page}`)
        } 
        else if(category == 'purchase'){
            // purchase report function call
            purchaseReport()
        }
        else if(category == 'voucher'){
            // purchase report function call
            voucherReport()
        }
        else if(category == 'sales'){
            // sales report function call
            salesReport()
        }
        else if(category == 'invoice'){
            // invoice report function call
            invoiceReport()
        }
        else if(category == 'expence_entries'){
            // expence entries function call
            expenceEntriesReport()
        }
        else if(category == 'bank_entries'){
            // bank entries function call
            bankEntriesReport()
        }
        else if(category == 'net_purchase'){
            // net purchase function call
            netPurchaseReport()
        }
        else if(category == 'net_sales'){
            // net sales function call
            netSalesReport()
        }
        else if(category == 'net_payable'){
            // net payable function call
            netPayableReport()
        }
        else if(category == 'net_reciveable'){
            // net recivalbe function call
            netReciveableReport()
        }
        else if(category == 'loan_management'){
            // loan management function call
            loanManagementReport()
        }
        else if(category == 'gst_details'){
            // gst detail function call
            gstDetailReport()
        }
    }

    function backResults(data){
        return data?.results
    }

    function LinkMethod(data, id){
        ph_data  = ''
        for(var i=0;i<data.length;i++){
                ph_data += `<a class="me-2" href="tel:${data[i]?.Phone_Number}" title="${data[i]?.Phone_Number}">${data[i]?.Phone_Number}</a>`
        }
        return ph_data
    }
    function SpanMethod(data, id){
        ph_data  = ''
        for(var i=0;i<data.length;i++){
            camma = i+1 < data.length ? ',' : ''
            ph_data += `<span>${data[i]?.Quality} - ${data[i]?.Price}${camma} </span>`
        }
        return ph_data 
    }
    function POMethod(data){
        ph_data  = ''
        for(var i=0;i<data.length;i++){
            camma = i+1 < data.length ? ',' : ''
            ph_data += `<div class="small">${i+1}. ${data[i]?.Material_Name} - <span title="Total quantity">${data[i]?.Quantity}</span> </div>`
        }
        return ph_data
    }
    function SalePOMethod(data, remainder, netdata){
        ph_data  = 0
        for(var i=0;i<data.length;i++){
            // camma = i+1 < data.length ? ',' : ''
            ph_data += Number(data[i]?.qty)
        }
        var sale_data = `<div>${data[0]?.MatId?.Material_Name} - <span title="Total quantity" class="text-success">${parseFloat(ph_data).toFixed(2)}</span> 
            <div class="small"><b>Remainder : </b> ${remainder?.GSTFilledInvNo } ( ${remainder?.GSTFilledInvReceive} )</div>
            <div class="small">
                <b>With GST : </b> ${parseFloat(netdata?.WithGSTNetTotalAmount).toFixed(2)}
                <b class="ms-2">With Out GST : </b> ${parseFloat(netdata?.WithOutGSTNetTotalAmount).toFixed(2)}<br>
                <b>Amount Payyed : </b> ${parseFloat(netdata?.AmountPayyed).toFixed(2)}
                <b class="ms-2">Balance : </b> ${parseFloat(netdata?.Balance).toFixed(2)}
            </div>
        </div>`
        return sale_data
    }
    // function InvoiceMethod(data){
    //     ph_data  = ''
    //     for(var i=0;i<data.length;i++){
    //         camma = i+1 < data.length ? ', &nbsp;' : ''
    //         ph_data += `<a class="text-blue" href="${data[i]?.id}">#${data[i]?.InvoiceNo}${camma} </a>`
    //     }
    //     return ph_data
    // }

    function apiData(url){
        var get_data = GetData(url)
 
        if (get_data?.detail == 'Invalid page.'){
            endof_api = true
            return 'invalid_data'
        }else{
            result = backResults(get_data)
            return result
        }
    }

    function agencyReport(){
        $('.reports thead ').html(`<tr><th>Name</th><th>Bank Detail</th><th>GST & PAN</th></tr>`)
        // get agency data
        var agency_info = apiData(agency_url)
        for(var i=0;i<agency_info.length;i++){
            $('.reports tbody').append(`
            <tr >
                <td>
                    <a href="${agency_info[i]?.id}">${agency_info[i]?.Name}</a>
                    <div><b>Email : </b><span>${agency_info[i]?.Email}</span></div>
                    <div><b>Phone : </b>${appendData(agency_info[i]?.Phone, 'Phone')}</div>
                    <div><b>Address : </b>${agency_info[i]?.Address },<br> ${agency_info[i]?.City}, ${agency_info[i]?.State}, ${agency_info[i]?.Zip}, ${agency_info[i]?.Country}</div>
                </td>
                <td>
                    ${appendBankDetail(agency_info[i]?.Bank_Account)}
                </td>
                <td>
                    <div><b>GST : </b>${agency_info[i]?.GST_Number}</div>
                    <div><b>PAN : </b>${agency_info[i]?.PAN_Number}</div>
                    <div><b>TIN : </b>${agency_info[i]?.Tin}</div>
                </td>
            </tr>`)
        }
        jsondatatable()
    }

    function appendBankDetail(bankinfo){
        let data = ''
        if(bankinfo.length != 0){
            bankinfo.forEach((e) => {
                data += `
                <div><b>Holder Name : </b>${e?.Account_Holder_Name} ( ${e?.Account_Holder_Position} )</div>
                <div>${e?.Account_Number}</div>
                <div><b>IFSC : </b>${e?.IFSC_Code} <b>Branch : </b>${e?.Branch}</div>
                <div class="border-bottom"><b>Bank Name : </b>${e?.Bank_Name} </div>`
            })
        }else{
            data = 'No Bank Entries.'
        }

        return data
    }

    function vendorReport(){
        $('.reports thead ').html(`<tr><th>Name</th><th>Company Name</th><th>Phone</th><th>Email</th><th>Payment Capabilities</th></tr>`)
        var vendor_info = apiData(vendor_url)
        for(var i=0;i<vendor_info.length;i++){
            $('.reports tbody').append(`<tr><td><a class="text-capitalize" href="${vendor_info[i]?.id}">${vendor_info[i]?.Vendor_Name}</a></td><td class="text-capitalize">${vendor_info[i]?.Company_Name}</td><td><a href="tel:${vendor_info[i]?.Phone}">${vendor_info[i]?.Phone}</a></td><td><a href="mailto:${vendor_info[i]?.Email}">${vendor_info[i]?.Email}</a></td><td class="text-capitalize">${vendor_info[i]?.Payment_Capabilities}</td></tr>`)
        }
        jsondatatable()
    }

    function customerReport(){
        $('.reports thead ').html(`<tr><th>Name</th><th>Company Name</th><th>Phone</th><th>Email</th><th>No Of Project</th></tr>`)
        var customer_info = apiData(customer_url)
        // console.log(customer_info)
        for(var i=0;i<customer_info.length;i++){
            email = customer_info[i]?.Company_Email == null ? '-' : `<a href="mailto:${customer_info[i]?.Email}">${customer_info[i]?.Company_Email}</a>`
            $('.reports tbody').append(`<tr ><td><a class="text-capitalize" href="${customer_info[i]?.id}">${customer_info[i]?.Founder_Name}</a></td><td class="text-capitalize">${customer_info[i]?.Company_Name}</td><td class="cus_${customer_info[i]?.id}">${LinkMethod(customer_info[i]?.Founder_Phone, customer_info[i]?.id)}</td><td>${email}</td><td>${customer_info[i]?.No_Of_Project}</td></tr>`)
        }
        jsondatatable()
    }

    function productReport(){
        $('.reports thead ').html(`<tr><th>Material Name</th><th>HSN Code</th><th>Price</th><th>GST</th></tr>`)
        var product_info = apiData(product_url)
        for(var i=0;i<product_info.length;i++){
            $('.reports tbody').append(`<tr><td><a class="text-capitalize" href="${product_info[i]?.id}">${product_info[i]?.Product}</a></td><td class="text-capitalize">${product_info[i]?.HSNCode}</td><td class="mp_${product_info[i]?.id}">${SpanMethod(product_info[i]?.Quality, product_info[i]?.id)}</td><td>${product_info[i]?.GST}</td></tr>`)
        }
        jsondatatable()
    }

    async function ordereport(){
        $('.reports thead ').html(`<tr><th>Order Id</th><th style="width: 20%;">Customer Name</th><th style="width:20%;">Delivery Address</th><th style="width:20%;">Billing Address</th><th>PO Materials</th></tr>`)
        var order_info = apiData(order_url)
        for(var i=0;i<order_info.length;i++){
            $('.reports tbody').append(`<tr>
            <td style="width: 8%;">
                <a class="text-capitalize" href="${order_info[i]?.id}">#${order_info[i]?.id}</a>
            </td>
            <td>
                <a  class="text-capitalize" href="${order_info[i]?.Sales_Company?.id}">${order_info[i]?.Sales_Company?.Company_Name}</a>
                <div class="small text-capitalize">Founder : ${order_info[i]?.Sales_Company?.Founder_Name}</div>
                <div>Email : ${order_info[i]?.Sales_Company?.Company_Email == null ? 'No data.' : order_info[i]?.Sales_Company?.Company_Email}</div>
                <div>Phone : ${appendData(order_info[i]?.Sales_Company?.Founder_Phone, 'Phone_Number')}</div>
            </td>
            <td class="text-capitalize">${order_info[i]?.Sales_Delivery_Address}</td>
            <td class="text-capitalize">${order_info[i]?.Billing_Address}</td>
            <td>${POMethod(order_info[i]?.PO_Number?.PO_Material_Info)}</td></tr>`)
        }
        jsondatatable()
    }

    function quotationReport(url){
        if(page == 1){
            $('.reports thead ').html(`<tr><th>S.No</th><th>Quotation Id</th><th>Order Id</th><th>Customer Name</th><th class="w-50">PO Materials</th></tr>`)
        }
        var data = apiData(url)
        if(data != 'invalid_data'){
            for(var i=0;i<data.length;i++){
                var s_no = page - 1 
                var s_n = s_no == 0 ? '' : s_no * 10 
                var no = Number(s_n) + Number(i) + 1
                $('.reports tbody').append(`<tr>
                <td>${no}</td>
                <td><a class="text-capitalize" href="${data[i]?.id}">#${data[i]?.id}</a></td>
                <td><a class="text-capitalize" href="${data[i]?.order?.id}">#${data[i]?.order?.id}</a></td>
                <td class="text-capitalize">${data[i]?.order?.Sales_Company?.Company_Name}</td>
                <td>${POMethod(data[i]?.order?.PO_Number?.PO_Material_Info)}</td></tr>`)
            }
        }else{
            $('.reports tfoot').html('<tr><th colspan="5" class="py-1">End Of List. !!!</th></tr>')
        }
        jsondatatable()
    }

    function purchaseReport(){    
        $('.reports thead ').html(`<tr><th style="width: 9%;">Purchase Id</th><th style="width: 10%;">Quotation Id</th><th style="width: 9%;">Order Id</th><th>Customer Name</th><th class="w-50">PO Materials</th></tr>`)
        var data = apiData(purchase_url)
        // console.log(data)
        for(var i=0;i<data.length;i++){
            $('.reports tbody').append(`<tr>
            <td><a class="text-capitalize" href="${data[i]?.id}">#${data[i]?.id}</a></td>
            <td><a class="text-capitalize" href="${data[i]?.quotation?.id}">#${data[i]?.quotation?.id}</a></td>
            <td><a class="text-capitalize" href="${data[i]?.quotation?.order?.id}">#${data[i]?.quotation?.order?.id}</a></td>
            <td >
                <a href="${data[i]?.customerId?.id}" class="text-capitalize">${data[i]?.customerId?.Company_Name}</a>
                <div class="text-capitalize">Founder : ${data[i]?.customerId?.Founder_Name}</div>
                <div>Email : ${data[i]?.customerId?.Company_Email == null ? 'No data.' : data[i]?.customerId?.Company_Email}</div>
                <div>Phone : ${appendData(data[i]?.customerId?.Founder_Phone, 'Phone_Number')}</div>
            </td>
            <td>${POMethod(data[i]?.quotation?.order?.PO_Number?.PO_Material_Info)}</td></tr>`)
            // console.log(data[i])
        }
        jsondatatable()
    }

    // on progress
    function voucherReport(){
        $('.reports thead ').html(`
        <tr>
            <th>Voucher Id</th>
            <th>Vendor Name</th>
            <th>Order Id</th>
            <th>Customer Name</th>
            <th class="w-50">PO Materials</th>
        </tr>`)
        var data = apiData(voucher_url)
        // console.log(data)
        for(var i=0;i<data.length;i++){
            $('.reports tbody').append(`<tr>
            <td><a class="text-capitalize" href="${data[i]?.id}">#${data[i]?.id}</a></td>
            <td>
                <a class="text-capitalize" href="${data[i]?.VendorId?.id}">${data[i]?.VendorId?.Company_Name}</a>
                <div><b>Ac No :</b> ${data[i]?.vendorDetail?.AcNumber}</div>
                <div><b>Bank :</b> ${data[i]?.vendorDetail?.Bank}<b class="ms-1">IFSC :</b> ${data[i]?.vendorDetail?.IFSC}</div>
                <div><b>GST No :</b> ${data[i]?.vendorDetail?.GSTNo}</div>
            </td>
            <td><a class="text-capitalize" href="${data[i]?.quotation?.order?.id}">#${data[i]?.quotation?.order?.id}</a></td>
            <td class="text-capitalize">
                <a href="${data[i]?.quotation?.order?.Sales_Company?.id}">${data[i]?.quotation?.order?.Sales_Company?.Company_Name}</a>
                <div>Founder : ${data[i]?.quotation?.order?.Sales_Company?.Founder_Name}</div>
                <div>Email : ${data[i]?.quotation?.order?.Sales_Company?.Company_Email}</div>
            </td>
            <td>${voucherAmount(data[i]?.amount)}</td></tr>`)
        }
        jsondatatable()
    }

    function voucherAmount(amount){
        var data = ''
        for(var i=0;i<amount.length;i++){
            var purchase = amount[i]?.VoucherMaterialInfo

            var purchase_material_qty = 0
            for(var j=0;j<purchase.length;j++){
                purchase_material_qty += Number(purchase[i]?.QtyCalc)
            }
            // console.log(amount[i])
            data += `
                <div class="mb-1 border border-rounded p-1">
                    <b class="me-1">${i+1}. </b>${purchase[i]?.MaterialName} ( ${parseFloat(purchase_material_qty).toFixed(2)} )
                    <div class="small">
                        <b class="">Amount :</b> ${parseFloat(amount[i]?.total).toFixed(2)}
                        <b class="ms-2">CGST :</b> ${parseFloat(amount[i]?.cgst_amount).toFixed(2)}
                        <b class="ms-2">SGST :</b> ${parseFloat(amount[i]?.sgst_amount).toFixed(2)}
                        <b class="ms-2">Total :</b> ${parseFloat(amount[i]?.total_amount).toFixed(2)}
                    </div>
                </div>
            `
        }
        return data
    }

    function salesReport(){  

        $('.reports thead ').html(`<tr><th>Sales Id</th><th>Order Id</th><th>Customer</th><th class="w-50">PO Materials</th></tr>`)
        var data = apiData(sales_url)
        for(var i=0;i<data.length;i++){
            $('.reports tbody').append(`<tr>
            <td><a class="text-capitalize" href="${data[i]?.id}">#${data[i]?.id}</a></td>
            <td><a class="text-capitalize" href="${data[i]?.orderid?.id}">#${data[i]?.orderid?.id}</a></td>
            <td class="text-capitalize">
                <a class="text-capitalize" href="${data[i]?.customer?.customerid?.id}">${data[i]?.customer?.customerid?.Company_Name} ( ${data[i]?.customer?.customerid?.Founder_Name} )</a>
                <div class="small">
                    <b>Phone : </b>${data[i]?.customer?.phone?.Phone_Number}<br>
                    <b>GST No : </b>${data[i]?.customer?.gst?.GST_No}<br>
                    <b>PAN No : </b>${data[i]?.customer?.pan?.PAN_No}<br>
                    <b>TIN No : </b>${data[i]?.customer?.tin?.TIN_No}
                </div>
            </td>
            <td>${SalePOMethod(data[i]?.poInfo, data[i]?.remainder, data[i]?.netAmount)}</td></tr>`)
        }
        jsondatatable()
    }

    async function invoiceReport(){
        $('.reports thead ').html(`<tr><th style="width: 8%;">Invoice Id</th><th style="width: 8%;">Sales Id</th><th style="width: 8%;">Order Id</th><th style="width: 35%;">Customer Name</th><th class="w-50">Invoices</th></tr>`)
        var data = apiData(invoice_url)
        for(var i=0;i<data.length;i++){
            $('.reports tbody').append(`<tr>
            <td><a class="text-capitalize" href="${data[i]?.id}">#${data[i]?.id}</a></td>
            <td class="text-capitalize"><a class="text-capitalize" href="${data[i]?.saleid?.id}">#${data[i]?.saleid?.id}</a></td>
            <td><a class="text-capitalize" href="${data[i]?.orderid}">#${data[i]?.orderid}</a></td>
            <td>
                <a class="text-capitalize" href="${data[i]?.saleid?.customer?.customerid?.id}">${data[i]?.saleid?.customer?.customerid?.Company_Name} (${data[i]?.saleid?.customer?.customerid?.Founder_Name})</a>
                <div><b >phone : </b>${data[i]?.saleid?.customer?.phone?.Phone_Number}<b class="ms-2">PAN No : </b>${data[i]?.saleid?.customer?.pan?.PAN_No}</div>
                <div><b >TIN No : </b> ${data[i]?.saleid?.customer?.tin?.TIN_No}<b class="ms-2">GST No : </b>${data[i]?.saleid?.customer?.gst?.GST_No}</div>
            </td>
            <td>
                Invoice No : ${data[i]?.InvoiceNo} <small>( ${data[i]?.InvoiceDate} )</small>
                <hr class="my-1"/>
                ${DCMethod(data[i]?.DC)}
            </td>
            </tr>`)
        }
        jsondatatable()
    }


    // dc method
    function DCMethod(dc){
        var data = ''

        dc.forEach(e => {
            data += `<div>
                Material : ${e?.material_name}
                <div><b >Quantity : </b>${parseInt(e?.quantity).toFixed(2)} <b class="ms-2">Amount : </b>${parseInt(e?.amount).toFixed(2)}</div>    
            </div>`
        })

        return data
    }


    function expenceEntriesReport(){}


    function bankEntriesReport(){}


    function netPurchaseReport(){}


    function netSalesReport(){}


    function netPayableReport(){}


    function netReciveableReport(){}


    function loanManagementReport(){}


    function gstDetailReport(){}
    

    function randomClass() {
        var S4 = function() {
           return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
        };
        return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
    }

    function jsondatatable(){
        $('#reporttable').DataTable().destroy();
        $('#reporttable').DataTable( {
            dom: 'Bfrtip',
            buttons: [
                'copy', 'csv', 'excel', 'pdf', 'print'
            ]
        })
        setInterval( function () {
            $('#reporttable').ajax.reload();
        }, 3000 );  
    }


    function appendData(data, col){
        let values = ''
        let d_l = data.length
        i = 0
        if(d_l != 0){
            data.forEach((e) => {
                values += `<span class="me-1">${e[col]},</span>`
            })
        }else{
            values = `No data.`
        }

        return values
    }

})