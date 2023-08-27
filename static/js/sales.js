var exampleModal = document.getElementById('purchaseEntry')

var quotation_id
var order_id
var quotation_data
var append_ids = 0
var Vendor_ID = 0
var new_payment_fun = false
var purchase_response = false
var signatures = GetData(`${url}signature/`)
var prepared_by = false
var approved_by = false
var passed_by = false

 
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    append_ids = 0
    // console.log('works')

    quotation_id = button.getAttribute('quotation-id')
    mat_id = button.getAttribute('mat-id')

    // console.log(quotation_id)
    if(quotation_id){
        var quotation_url = `${url}quotations/${quotation_id}`
        var quo_data = GetData(quotation_url)
        order_id = quo_data?.order?.id
        for(var i=0;i<quo_data?.vendorInfo.length;i++){
            if(mat_id == quo_data?.vendorInfo[i]?.id){
                var mat = quo_data?.vendorInfo[i]?.mat_id
                // console.log(mat)
                $(this).attr('mat-id', mat)
            }
        }

        var purchase_entry_url = `${url}purchase-entry/?quotation=${quotation_id}`
        var p_data =  GetData(purchase_entry_url)

        var materials_entries = []
        if(p_data?.count != 0){
            var p_res = p_data?.results[0]
            purchase_response = true
            // console.log(p_res)
            var p_entries = p_res?.entries
            for(var i=0;i<p_entries.length;i++){
               var ent =  p_entries[i]?.purchaseMaterial
            //    // console.log(ent)
               for(var j=0;j<ent.length;j++){
                   
                materials_entries.push(ent[j])
               }
            }
            // console.log(p_entries)
        }

    }

    var mat_po = $(this).attr('mat-id')
    let mat_info = mat_po.split(',')

    var vendor_materials = []
    for(var i=0;i< mat_info.length;i++){
        var material_info_url = url+'material-info/'+mat_info[i]+'/'
        var data = GetData(material_info_url)
        vendor_materials.push(data)
    }

    // console.log(vendor_materials)

    const vendor = vendor_materials[0]?.Vendor

    const vendor_id = vendor?.id
    Vendor_ID = vendor_id
    const vendor_name = vendor?.Vendor_Name
    const vendor_company_name = vendor?.Company_Name

 
    var action_url = url+'quotations/'+quotation_id+'/'
    var data = GetData(action_url)
    quotation_data = data

    var sales = data?.sales
    const customer_info = sales?.customer
    let customer_id = customer_info?.id
    let customer_name = customer_info?.Founder_Name
    let company_name = customer_info?.Company_Name

    var purchase = data?.purchase
    var Branches = sales?.customer?.Branches

    var deliveryAddress = data?.order?.Sales_Delivery_Address.split(',')[0]
    var PurchaseEntry
    var NickName 
    for(var i=0;i<Branches.length;i++){
        var da = Branches[i]?.Delivery_Address
        if(da.length != 0){

            for(var j=0;j<da.length;j++){
                var d = da[j]
                if(d.Address.includes(deliveryAddress) == true){
                    NickName = da[0]?.NickName 
                }
            }

        }

    }

    $('#purchaseEntry #vendor_name').html(`${vendor_name}`).attr('vendor-id', vendor_id)
    $('#purchaseEntry #salesDetail').html(`
        <div>
        <b>Sales : </b>
        <span id="customer_id" customer-id="${customer_id}">${customer_name}</span>
        <span id="nickName" class="mx-2 text-primary">( ${NickName} )</span>
        <b>Company Name : </b>
        <span>${company_name}</span>
        </div>
        <div class="fa-16 mt-2 text-success"><b>Vendor Info : </b></div>
        <div class="text-capitalize"><b>Vendor Name : </b> <span>${vendor_name}</span> ( ${vendor_company_name} )</div>
    `)
    $('#purchase_tbl').html(``)


    for(var i=0;i<vendor_materials.length;i++){
        let vm = vendor_materials[i]
        // console.log(vm)
        // console.log(vm)
        var qt = Enc_QuantityType(vm?.Quantity_Type)
        var total = Number(vm?.Quantity) * Number(vm?.Final_Offer_Price)
        // gst calculation starts here
        let gst_p = vm?.Product_Name?.GST
        gst_price = gst_p.split('%')
        var gst_price = total * Number(gst_price[0])/100
        var withGst = gst_price + total

        // purchase entry is check already done
        PurchaseEntry = vm?.Purchase_Entry


        if(purchaseEntry == true){

        }else{

            $('#main_po_detail').append(`
                <tr class="upm_${i+1}">
                    <td>${i+1}</td>
                    <td>${vm?.Location_Supply}</td>
                    <td>At Site</td>
                    <td id="matname">${vm?.Material_Name}</td>
                    <td id="quantity" mat-id="${vm?.id}">${vm?.Quantity}</td>
                    <td>${qt}</td>
                    <td>
                        <button href="" 
                        vm-id="${vm?.id}"
                        vm-ls="${vm?.Location_Supply}" 
                        vm-mn="${vm?.Material_Name}" 
                        vm-qty="${vm?.Quantity}" 
                        vm-qty-type="${vm?.Quantity_Type}" 
                        vm-qt="${qt}" 
                        vm-round="${Math.round(vm?.Final_Offer_Price)}"
                        vm-fop="${vm?.Final_Offer_Price}" 
                        vm-total="${vm?.total}" 
                        vm-gst="${vm?.Product_Name?.GST}" 
                        vm-withgst="${withGst}"  
                        class="fa-12 btn btn-sm btn-primary append_mat_data mid${vm?.id} py-0 w-100"><i class="fa fa-plus fa-12"></i> &nbsp;Add</button></td>
                </tr>
            `)
        
        }


    }

    append_mat_po_data('#purchaseEntry #purchase_tbl' , '', 'pm_')
    

})


var added_purchase_id = []

// add purchase entry functionalities
async function AddPurchaseEntry(refresh){

    if(refresh == false){
        $('#purchase_entry_btn').click(async function (){
            // console.log('refresh : ',refresh)
            // console.log(split_invoice_data)
            // console.log(invoice_d)

            var purchase_entry_urls = `${base}post-api/purchase-entry/?quotation=${quotation_id}&vendorId=${Vendor_ID}`
            var purchase_datas = GetData(purchase_entry_urls)
            // console.log(purchase_datas)
            // console.log(invoice_d)
            for(var i=0;i<invoice_d;i++){
                var purchase_entry = split_invoice_data[i]
                var material_id = split_invoice_data[i]?.mat_id
                var purchase_entry_update = {
                    'Purchase_Entry': true
                }
                var purchase_update_url = `${base}post-api/material-info/${material_id}/`
                await PurchasePatchMethod(purchase_entry_update, purchase_update_url)
                await SplitPurchaseEntries(purchase_entry)
            }

            split_invoice_data = []
            invoice_d = []
            // console.log(added_purchase_id)
    
            var net_id
            await PostNetData().then((value) =>  net_id = value)
            var remainder_id 
            await PostRemainderData().then((value) =>  remainder_id = value)
            var Vendor_id = Number($('#vendor_name').attr('vendor-id'))

            var single_purchase_param = {
                "vendorId": Number($('#vendor_name').attr('vendor-id')),
                "customerId": Number($('#customer_id').attr('customer-id')),
                "remainder": remainder_id,
                "netAmount": net_id,
                "purchaseMaterial": added_purchase_id,
                "quotation": quotation_id
            }
            var sp_id 
            await SinglePurchase(single_purchase_param).then((value) => sp_id = value)
            

            if (purchase_datas?.count == 0){
                var order = {
                    "order": order_id,
                    "quotation": Number(quotation_id),
                    "entries": [sp_id],
                    "vendorId": Vendor_ID
                }
                var purchase_entry_url = base+"post-api/purchase-entry/"  
                await PurchasePostFunction(purchase_entry_url, order)
                $('#remainder_data')[0].reset();
                $('.net_remainder #withoutgsttotalamount, .net_remainder #withgsttotalamount, .net_remainder #amountpayyed, .net_remainder #balanceamount').val('')
                $('#remainder_data, .net_remainder, #purchase_entry_btn').addClass('d-none')
                alert('Purchase added successfully. !!!')

            }else{

                var entries = purchase_datas?.results[0]?.entries
                var purchase_id = purchase_datas?.results[0]?.id
                var order = {
                    "entries": entries
                }
                var purchase_entry_url = base+"post-api/purchase-entry/"+purchase_id+"/"  
                var purchase_id = await PurchasePatchMethod(order, purchase_entry_url)
                alert('Purchase added successfully. !!!')

            }
            

        })
    }else{
        alert('all materials added. !!!')
    }



}
// add purchase Entries
async function SplitPurchaseEntries(params){
    var action_url = base+'post-api/purchase-material-entry/'
    var id = await PurchasePostFunction(action_url, params)
    added_purchase_id.push(id)
}
// net function
async function PostNetData(){
    var net_param = {
        WithOutGSTNetTotalAmount: $('#withoutgsttotalamount').val(),
        WithGSTNetTotalAmount: $('#withgsttotalamount').val(),
        AmountPayyed: $('#amountpayyed').val(),
        Balance: $('#balanceamount').val(),
    }
    var net_url = base+'post-api/purchase-net-amount/'
    var net_id = await PurchasePostFunction(net_url, net_param)

    return net_id
}
// remainder Function
async function PostRemainderData(){
    var form = $("#remainder_data");
    var formData = new FormData(form[0]);
    var remainder_url = base+'post-api/purchase-remainder/'
    var remainder_id = await PurchaseFormSubmit(remainder_url, formData)
    return remainder_id
}
// single purchase
async function SinglePurchase(single_purchase_param){
    var action_url = base+'post-api/single-purchase-entry/'
    var single_id = await PurchasePostFunction(action_url, single_purchase_param)
    return single_id
}
// append mat po data
function append_mat_po_data(select, new_data, slct){

    $('.append_mat_data').click(function(e){
        e.preventDefault()

        $('.append_submit, #purchase_tabels').removeClass('d-none')

        append_ids += 1

        let vm_id = $(this).attr('vm-id')
        // console.log(vm_id)
        let vm_mat_id = $(this).attr('vm-mat-id')
        let vm_ls = $(this).attr('vm-ls')
        let vm_mn = $(this).attr('vm-mn')
        let vm_qty_type = $(this).attr('vm-qty-type')
        let vm_qt = $(this).attr('vm-qt')
        let vm_fop = $(this).attr('vm-fop')
        let vm_gst = $(this).attr('vm-gst')
        let single_id = $(this).attr('single_id')

        // console.log(single_id)
        $(select).append(`
            <tr class="${slct}${append_ids}" data="${new_data}">
                <td hidden><input type="text" id="mat_id" single_id="${single_id}"  data-mat="${vm_id}" value="new"></td>
                <td><input type="date" id="purchase_date" data-col="PurchaseDate" style="width: 115px;"></td>
                <td><div style="width: 140px;" id="location_supply">${vm_ls}</div></td>
                <td><div style="width: 40px;" id="site" data-col="Site">At Site</div></td>
                <td><div style="width: 100px;" id="matname" data-col="MaterialName">${vm_mn}</div></td>
                <td><input type="text" id="cdc" data-col="CDC" placeholder="CDC"></td>
                <td><input type="text" id="ldc" data-col="LDC" placeholder="LDC"></td>
                <td><input type="text" id="vehicle_no" data-col="VehicleNo" placeholder="Vehicle No"></td>
                <td><input type="number" class="quantity quantity${append_ids}" data-col="Quantity" placeholder="qty" style="width:45px;"></td>
                <td><div id="quantity_type" style="width:40px;" >${vm_qt}</div></td>
                <td><input type="text" class="quantity_calculation" mat_id="${append_ids}" data-col="Quantity_val" placeholder="QTY formula" style="width:100px;"></td>
                <td><input type="text" class="res${append_ids} res" placeholder="QTY Calc" style="width:100px;"></td>
                <td><input type="text" id="round_off" class="roundoff${append_ids}" data-col="RoundOff" placeholder="Round Off" style="width:60px;" ></td>
                <td><div style="width:40px;" class="rate${append_ids}" id="rate">${vm_fop}</div></td>
                <td><input type="text" id="total" class="total${append_ids}" data-col="Total" placeholder="Total" style="width:60px;" ></td>
                <td><div style="width:40px;" class="gst${append_ids}" id="gst">${vm_gst}</div></td>
                <td><input type="text" id="with_gst" class="withgst${append_ids}" data-col="with_gst" placeholder="With GST"  style="width:60px;"></td>
                <td><input type="text" id="site_supervisior" data-col="SiteSupervisior" placeholder="Site Supervisior"></td>
                <td><input type="text" id="qc" data-col="QC" placeholder="QC"></td>
                <td><input type="text" id="security" data-col="Security" placeholder="Security"></td>
                <td><input type="text" id="engineer" data-col="Engineer" placeholder="Engineer"></td>
                <td><input type="text" id="driver_name" data-col="DriverName" placeholder="Driver Name"></td>
                <td><input type="text" id="unloading_supervisior" data-col="UnloadingSupervisior" placeholder="Unloading Supervisior"></td>
            </tr>
        `)

        OnchangeCall()
        // OnPurchaseSubmit()

    })
    
}
// checked signature
function CheckedSignature(){
    $('.check_signature').click(function(e){
        e.preventDefault()
        var name_cls = $(this).attr('name')
        var date_cls = $(this).attr('date')
        var column_cls = $(this).attr('column')
        var name_d = $(`.${name_cls}`).val()
        var date_d = $(`.${date_cls}`).val()
        if(column_cls == 'approved_by_col'){
            approved_by = true
        }else if(column_cls == 'passed_by_col'){
            passed_by = true
        }else{
            prepared_by = true
        }

        if(name_d != '' && date_d != ''){
            var d = signatures?.results.filter(p => p.id == name_d)
            $(`.${column_cls}`).html(`
                <img src="${d[0]?.signature}" data-id="${d[0]?.id}" width="200px" height="70px" class="mt-3"/>
            `)
        }else{
            alert('Name & Date cannot be empty. !!!')
        }
    })
}
// cgst calculation
function CGSTCalculation(total, percentage){
    let per = percentage/100 
    let ttl = total * per
    return ttl
}
// sgst calculation
function SGSTCalculation(total, percentage){
    let per = percentage/100 
    let ttl = total * per
    return ttl
}



// purchase post function
function PurchasePostFunction(action_url, data){
    var data;
    $.ajax({
        type: "POST",
        url: action_url,
        contentType: "application/json",
        dataType: "json",
        async: false,
        data: JSON.stringify(data),
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (response) {
            data = response?.id
        },
        error: function (response) {
            // console.log(response);
        }
    });
    return data
}
function PurchaseFormSubmit(action_url, Formdata){
    var data;
    $.ajax({
        url: action_url,
        type: 'POST',
        data: Formdata,
        async: false,
        success: function (response) {
            data = response?.id
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        cache: false,
        contentType: false,
        processData: false
    });
    return data
}
// purchase patch method
function PurchasePatchMethod(params, dynamicurl) {
    $.ajax({
        type: 'PATCH',
        url: dynamicurl,
        data: JSON.stringify(params),
        processData: false,
        contentType: "application/json",
        dataType: "json",
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (response) {

        },
        error: function (response) {
            alert('Network issue Try again later. !!!')
        }
    });
}

function OnchangeCall(){
    $('.quantity_calculation').change(function (){
        var qty_formula = $(this).val()
        // console.log(qty_formula)
        var evaluation = eval(qty_formula)


        var mat_id = Number($(this).attr('mat_id'))
        // console.log(mat_id)
        var qty = Number($(`.quantity${mat_id}`).val())
        evaluation = evaluation * qty
        var rate = Number($(`.rate${mat_id}`).text())
        
        $(`.res${mat_id}`).val(evaluation)

        var total = evaluation * rate
        $(`.total${mat_id}`).val(total)

        var gst = $(`.gst${mat_id}`).text()
        var gst_per = gst.replace('%', '')
        var gst_percentage = Number(gst_per) / 100
        var with_gst = gst_percentage * total
        $(`.withgst${mat_id}`).val(with_gst)
        
        var strevl = String(evaluation)
        // console.log(strevl)
        var round_off = strevl.substring(strevl.indexOf('.') + 1);
        round_off = Number(round_off)
        // console.log(round_off)
        $(`.roundoff${mat_id}`).val(round_off)


    })
}

var purchase_order = []

var  po_submit = document.getElementById('po_submit')
po_submit.addEventListener('click', function call(){
    $('.append_submit').addClass('d-none')
    $('#main_po_detail .append_mat_data').attr('disabled', true)
    // console.log(append_ids)
    for(var i=0;i<append_ids;i++){
        var selector = `.pm_${i+1}`
        var params = {
            "mat_id": $(`${selector} #mat_id`).attr('data-mat'),
            "PurchaseDate": $(`${selector} #purchase_date`).val(),
            "UnloadingSite": $(`${selector} #location_supply`).html(),
            "Site": $(`${selector} #site`).html(),
            "MaterialName": $(`${selector} #matname`).html(),
            "CDC": $(`${selector} #cdc`).val(),
            "LDC": $(`${selector} #ldc`).val(),
            "VehicleNo": $(`${selector} #vehicle_no`).val(),
            "Quantity": $(`${selector} .quantity`).val(),
            'QtyFormula': $(`${selector} .quantity_calculation`).val(),
            'QtyCalc': $(`${selector} .res`).val(),
            "QuantityType": $(`${selector} #quantity_type`).html(),
            "RoundOff": $(`${selector} #round_off`).val(),
            "Rate": $(`${selector} #rate`).html(),
            "Total": $(`${selector} #total`).val(),
            "GST": $(`${selector} #gst`).html(),
            "WithGST": $(`${selector} #with_gst`).val(),
            "SiteSupervisior": $(`${selector} #site_supervisior`).val(),
            "QC": $(`${selector} #qc`).val(),
            "Security": $(`${selector} #security`).val(),
            "Engineer": $(`${selector} #engineer`).val(),
            "DriverName": $(`${selector} #driver_name`).val(),
            "UnloadingSupervisior": $(`${selector} #unloading_supervisior`).val(),
        }
        purchase_order.push(params)

    }
    // for(var j=0;j<purchase_order.length;j++){

    // }
    // console.log(purchase_order)
    
    $('.po_table_data').html('')
    for(var i=0;i<purchase_order.length;i++){
        $('.po_table_data').append(`
            <div class="inv${i}">${purchase_order[i]?.MaterialName} - ${purchase_order[i]?.CDC } <b class="ms-2">Vehicle No : </b> : ${purchase_order[i]?.VehicleNo} <b class="ms-2">Qty : </b> ${purchase_order[i]?.Quantity} <b class="ms-2">Total :</b> ${purchase_order[i]?.Total} <a href="${i}" class=" ms-2 add_invoice" ><i class="fa fa-plus"></i></a></div>
        `)
    }

    addInvoice()

})

var split_invoice_data = []
var invoice_d = 0
var refresh_page = false

function addInvoice(){
    $(`.add_invoice`).click(function(e){
        // console.log(split_invoice_data)
        $('#remainder_data')[0].reset()
        $('.net_remainder #withoutgsttotalamount, .net_remainder #withgsttotalamount, .net_remainder #amountpayyed, .net_remainder #balanceamount').val('')
        e.preventDefault()
        var mat_id = $(this).attr('href')
        // console.log(mat_id)
        $(this).html('<i class="fa fa-check"></i>')
        var d = purchase_order[mat_id]
        split_invoice_data.push(d)
        invoice_d += 1
        $('#remainder_data, #make_new_payment, #purchaseEntry .modal-footer, .net_remainder, #purchase_entry_btn').removeClass('d-none')

        if(invoice_d >= append_ids){
            refresh_page = true
        }else{
            refresh_page = false
        }
        
    })
    // AddPurchaseEntry(refresh_page)

}

