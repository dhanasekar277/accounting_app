var quotation_id;
var quotation_data;
var append_ids = 0;
var new_payment_fun = false;

var signatures = GetData(`${url}signature/`);
var prepared_by = false;
var approved_by = false;
var passed_by = false;

var myMat = location.search.split("mat-id=")[1];
if (myMat) {
  let material_data = GetData(`${url}single-purchase-entry/${myMat}/`);
  // console.log(material_data)
  let purchase_material = material_data?.purchaseMaterial;

  var mat_ids = purchase_material.map((p) => p.mat_id);
  let mids = mat_ids.filter((v, i, a) => a.findIndex((t) => t === v) === i);
  $(".quotation_views").attr("mat-data", mids);
}

var purchase_length = 0;

var addvoucher = document.getElementById("addvoucher");
addvoucher.addEventListener("show.bs.modal", function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget;
  var mat_data = button.getAttribute("mat-data");
  quotation_id = button.getAttribute("quotation-id");
  $(`#ac_number, #bank, #ifsc, #mobile, #gst_no`).val("");
  $(`#bank_account`).html("");
  $(`#pan_detail, #voucher_tbl`).html("");

  if (quotation_id) {
    var purchase_url = `${url}purchase-entry/?quotation=${quotation_id}`;
    var purchase_data = GetData(purchase_url);
    // console.log(purchase_data)
    purchase_data = purchase_data?.results[0];
    var vendor_info = purchase_data?.entries[0]?.vendorId;
    purchase_data = purchase_data?.entries;
    // console.log(purchase_data)
    var quotation_data = purchase_data?.quotation;

    var purchase_entries_length = purchase_data.length;
    var purchase_entries = purchase_data;
    // console.log(purchase_entries)

    let v_company = vendor_info?.Company_Name.slice(0, 2).toUpperCase();

    for (var i = 0; i < purchase_entries.length; i++) {
      // console.log(purchase_entries[i]);
      var gst = purchase_entries[i]?.purchaseMaterial[0]?.GST;
      gst = Number(gst);
      // console.log(gst);

      let v_count = GetData(`${base}vouchers/voucher-count/${vendor_info?.id}`);
      voucher_count = v_count?.count + 1;
      let generate_voucher_id = `VC-${v_company}-${vendor_info?.id}-${
        voucher_count + i
      }`;
      let voucher_sl_no = v_count?.total_voucher + i;
      voucher_sl_no += 1;

      var total = purchase_entries[i]?.purchaseMaterial;
      var ttl = 0;
      for (var j = 0; j < total.length; j++) {
        ttl += Number(total[j]?.Total);
        var entry_pur_id = purchase_entries[i]?.purchaseMaterial;
        entry_pur_id = entry_pur_id.map((p) => p.id);
        // console.log(entry_pur_id)
      }
      // console.log(ttl)

      $(".purchase_amounts").append(
        `
                <div class="card px-2 py-2 mb-3 bg-light">
                <div class="col-12 materialName text-success mb-1" >
                    ${
                      purchase_entries[i]?.purchaseMaterial[0]?.MaterialName
                    } - <b class="text-danger">GST : ${gst}%</b> 
                </div>
                <div class="row row${i}" pur_mat_id="${entry_pur_id}">

                    <div class="col-6">
                        <div class="row">
                            <div class="col-6 mb-1">
                                <label for="" class="fw-bold">Voucher Date</label>
                                <input type="date" class="form-control form-control-sm" id="voucher_date" name="voucher_date">
                            </div>
                            <div class="col-6 mb-1 ps-0">
                                <label for="" class="fw-bold">Voucher No</label>
                                <input type="text" class="form-control vc${i} form-control-sm" id="voucher_no" name="voucher_no">
                            </div>
                            <div class="col-4 mb-1 pe-0">
                                <label for="" class="fw-bold">Voucher SL No</label>
                                <input type="text" class="form-control vs${i} form-control-sm" id="voucher_sl_no" name="voucher_sl_no">
                            </div>
                            <div class="col-4 mb-1 pe-0">
                                <label for="" class="fw-bold">PUR GST Invoice No</label>
                                <input type="text" class="form-control form-control-sm" value="${
                                  purchase_entries[i]?.remainder?.GSTFilledInvNo
                                }" id="invoice_no" name="invoice_no">
                            </div>
                            <div class="col-4 mb-1">
                                <label for="" class="fw-bold">Debit Voucher No</label>
                                <input type="text" class="form-control form-control-sm" id="debit_voucher_no" name="debit_voucher_no">
                            </div>
                        </div>
                    </div>

                    <div class="col-6">
                        <div class="row mb-2">
                            
                            <div class="col-lg-6 pe-0">
                                <label for="" class="fw-bold">Total</label>
                                <input type="text" class="form-control form-control-sm mainttl${i}" id="main_total" name="total">
                            </div>
                            <div class="col-lg-6">
                                <label for="" class="fw-bold">CGST(${
                                  gst / 2
                                }%): Amount</label>
                                <input type="text" class="form-control form-control-sm cgst_total${i}" id="cgst_total" name="cgst_total">
                            </div>
                            <div class="col-lg-6 mt-2 pe-0">
                                <label for="" class="fw-bold">SGST(${
                                  gst / 2
                                }%): Amount</label>
                                <input type="text" class="form-control form-control-sm sgst_total${i}" id="sgst_total" name="sgst_total">
                            </div>
                            <div class="col-lg-6 mt-2">
                                <label for="" class="fw-bold">Total Amount</label>
                                <input type="text" class="form-control form-control-sm total_amount${i}" id="total_amount" name="total-amount">
                            </div>
                        </div>
                    </div>

                </div>
                </div>

                `
      );

      $(`.vc${i}`).val(generate_voucher_id).attr("disabled", true);
      $(`.vs${i}`).val(voucher_sl_no).attr("disabled", true);

      var cgst_ = CGSTCalculation(ttl, gst / 2);
      $(`#addvoucher .cgst_total${i}`).val(cgst_);
      var sgst_ = SGSTCalculation(ttl, gst / 2);
      $(`#addvoucher .sgst_total${i}`).val(sgst_);
      var total_am = ttl + cgst_ + sgst_;
      $(`#addvoucher .total_amount${i}`).val(total_am);
      $(`#addvoucher .mainttl${i}`).val(ttl);
    }

    var purchase_material = purchase_data.map((p) => p.purchaseMaterial);
    var pm_data = [];

    for (var i = 0; i < purchase_material.length; i++) {
      var pm = purchase_material[i];
      // console.log(pm)

      for (var j = 0; j < pm.length; j++) {
        pm_data.push(pm[j]);
      }
    }
    var main_total = 0;
    pm_data.forEach((p) => {
      // console.log(p);
      $(`#voucher_tbl`).append(`
            <tr>
                <td>${p?.PurchaseDate}</td>
                <td>${p?.UnloadingSite}</td>
                <td>${p?.Site}</td>
                <td>${p?.MaterialName}</td>
                <td>${p?.CDC}</td>
                <td>${p?.LDC}</td>
                <td class="text-uppercase">${p?.VehicleNo}</td>
                <td>${p?.QtyCalc}</td>
                <td>${p?.QuantityType}</td>
                <td>${p?.RoundOff}</td>
                <td>${p?.Rate}</td>
                <td>${Number(p?.Total).toFixed(2)}</td>
            </tr>
            `);
      main_total += Number(p?.Total);
    });
    // console.log(pm_data)

    console.log(vendor_info)
    const vendor_name = vendor_info?.Vendor_Name;
    const vendor_gst = vendor_info?.GST_No;
    const vendor_pan = vendor_info?.PAN_No;

    if (vendor_gst.length != 0) {
      $(`#ac_number`).val(vendor_gst[0]?.Account_Number);
      $(`#bank`).val(vendor_gst[0]?.Bank_Account);
      $(`#ifsc`).val(vendor_gst[0]?.IFSC);
      $(`#trade_name`).val(vendor_gst[0]?.Trade_Name);
      $(`#mobile`).val(vendor_gst[0]?.Phone);
      // $(`#gst_no`).val(vendor_gst[0]?.GST_No)
      vendor_gst.forEach((el) => {
        $(`#gst_no`).append(`<option value="${el?.id}">${el?.GST_No}</option>`);
      });
    } else {
      for (var i = 0; i < vendor_gst.length; i++) {
        $(`#addvoucher #bank_account`).append(
          `<li>${vendor_gst[i]?.Account_Number} (${vendor_gst[i]?.Bank_Account} / ${vendor_gst[i]?.Branch})<a href="" class="add_gst" data-phone="${vendor_gst[i]?.Phone}" data-gst="${vendor_gst[i]?.GST_No}" data-an="${vendor_gst[i]?.Account_Number}" data-ifsc="${vendor_gst[i]?.IFSC}" data-bank="${vendor_gst[i]?.Bank_Account}"><i class="fa fa-plus fa-12 ms-2"></i></a></li>`
        );
      }
    }

    if (vendor_pan.length == 1) {
      $(`#pan_no`).val(vendor_pan[0]?.PAN_No);
    } else {
      for (var i = 0; i < vendor_pan.length; i++) {
        $(`#addvoucher #bank_account`).append(
          `<li>${vendor_pan[0]?.PAN_No} <a href=""><i class="fa fa-plus fa-12 ms-2"></i></a></li>`
        );
      }
    }

    $("#addvoucher #vendor_name").html(`${vendor_name} &nbsp;`);
    $("#addvoucher #voucher_name")
      .val(vendor_name)
      .attr("vendor-id", vendor_info?.id);
  }

  signatures?.results.forEach((ele) => {
    $(".signature_ip").append(`<option value="${ele.id}">${ele.name}</option>`);
  });

  AddToGst();
  AddVoucher(purchase_entries);
  CheckedSignature();
});

// checked signature
function CheckedSignature() {
  $(".check_signature").click(function (e) {
    e.preventDefault();
    var name_cls = $(this).attr("name");
    var date_cls = $(this).attr("date");
    var column_cls = $(this).attr("column");
    var name_d = $(`.${name_cls}`).val();
    var date_d = $(`.${date_cls}`).val();
    if (column_cls == "approved_by_col") {
      approved_by = true;
    } else if (column_cls == "passed_by_col") {
      passed_by = true;
    } else {
      prepared_by = true;
    }

    if (name_d != "" && date_d != "") {
      var d = signatures?.results.filter((p) => p.id == name_d);
      $(`.${column_cls}`).html(`
                <img src="${d[0]?.signature}" data-id="${d[0]?.id}" width="200px" height="70px" class="mt-3"/>
            `);
    } else {
      alert("Name & Date cannot be empty. !!!");
    }
  });
}

function CGSTCalculation(total, percentage) {
  let per = percentage / 100;
  let ttl = total * per;
  return ttl;
}

function SGSTCalculation(total, percentage) {
  let per = percentage / 100;
  let ttl = total * per;
  return ttl;
}

function UpdateVoucher(bi) {
  $("#voucher_entry_btn").click(function () {
    if ($("#addvoucher #voucher_date").val() && $("#addvoucher #debit_voucher_no").val()) {
      $(this).prop('disabled',true) 
      var base_info = {
        Name: $("#addvoucher #voucher_name").val(),
        AcNumber: $("#addvoucher #ac_number").val(),
        Bank: $("#addvoucher #bank").val(),
        IFSC: $("#addvoucher #ifsc").val(),
        Mobile: $("#addvoucher #mobile").val(),
        GSTNo: $("#addvoucher #gst_no").val(),
        PanNo: $("#addvoucher #pan_no").val(),
        VoucherDate: $("#addvoucher #voucher_date").val(),
        Trade_Name: $("#addvoucher #trade_name").val(),
        VoucherNo: $("#addvoucher #voucher_no").val(),
        VoucherSLNo: $("#addvoucher #voucher_sl_no").val(),
        InvoiceNo: $("#addvoucher #invoice_no").val(),
        DebitVoucherNo: $("#addvoucher #debit_voucher_no").val(),
      };
      var purchase_base_url = base + "post-api/voucher-base-info/" + bi + "/";
      PurchasePatchMethod(base_info, purchase_base_url);

      let total_param = {
        total: $("#addvoucher #main_total").val(),
        cgst_amount: $("#addvoucher #cgst_total").val(),
        sgst_amount: $("#addvoucher #sgst_total").val(),
        total_amount: $("#addvoucher #total_amount").val(),
        preparedDate: $("#addvoucher #prepared_by_date").val(),
        preparedName: $("#addvoucher #prepared_by_name").val(),
        approvedDate: $("#addvoucher #approved_by_date").val(),
        approvedName: $("#addvoucher #approved_by_name").val(),
        passedName: $("#addvoucher #passed_by_name").val(),
        passedDate: $("#addvoucher #passed_by_date").val(),
      };
      var total_url = base + "post-api/voucher-amount/";
      var id = PurchasePostFunction(total_url, total_param);
      // console.log(id)
    }else{
        alert('Voucher Date and Debit Voucher Number is required fields')
    }
  });
}

function AddToGst() {
  $(".add_gst").click(function (e) {
    $(`#bank_account`).html("");
    e.preventDefault();
    let gst = $(this).attr("data-gst");
    $("#addvoucher #gst_no").val(gst);
    let an = $(this).attr("data-an");
    $("#addvoucher #ac_number").val(an);
    let ph = $(this).attr("data-phone");
    $("#addvoucher #mobile").val(ph);
    let bank = $(this).attr("data-bank");
    $("#addvoucher #bank").val(bank);
    let ifsc = $(this).attr("data-ifsc");
    $("#addvoucher #ifsc").val(ifsc);
  });
}

// add voucher
function AddVoucher(po_entries) {
  $("#voucher_entry_btn").click(async function () {
    if ($("#addvoucher #voucher_date").val() && $("#addvoucher #debit_voucher_no").val() && approved_by == true && passed_by == true && prepared_by == true) {
      $(this).prop('disabled',true) 
      var voucher_vendor_info_param = {
        Name: $("#voucher_name").val(),
        AcNumber: $("#ac_number").val(),
        Bank: $("#bank").val(),
        IFSC: $("#ifsc").val(),
        Mobile: $("#mobile").val(),
        GSTNo: $("#gst_no").val(),
        PanNo: $("#pan_no").val(),
        TradeName: $("#trade_name").val(),
      };
      // console.log(voucher_vendor_info_param);

      var voucher_ven_url = `${base}post-api/voucher-vendor-info/`;
      var voucher_vendor_id = await PurchasePostFunction(
        voucher_ven_url,
        voucher_vendor_info_param
      );

      var Signature = [];
      var vchr_sig_url = base + "post-api/voucher-signature/";
      var sig_param_1 = {
        signature_name: 0,
        signature_id: $(".prepared_by_col img").attr("data-id"),
      };
      var sig_id = await PurchasePostFunction(vchr_sig_url, sig_param_1);
      Signature.push(sig_id);

      var sig_param_2 = {
        signature_name: 1,
        signature_id: $(".approved_by_col img").attr("data-id"),
      };
      var sig_id = await PurchasePostFunction(vchr_sig_url, sig_param_2);
      Signature.push(sig_id);

      var sig_param_3 = {
        signature_name: 2,
        signature_id: $(".passed_by_col img").attr("data-id"),
      };
      var sig_id = await PurchasePostFunction(vchr_sig_url, sig_param_3);
      Signature.push(sig_id);

      var total_ids = [];
      var voucher_ids = [];

      for (var i = 0; i < po_entries.length; i++) {
        // console.log(po_entries[i]);
        var p_id = po_entries[i]?.purchaseMaterial.map((p) => p.id);
        // console.log(p_id);

        var select = `.row${i}`;

        let voucher_param = {
          VoucherDate: $(`${select} #voucher_date`).val(),
          VoucherNo: $(`${select} #voucher_no`).val(),
          VoucherSLNo: $(`${select} #voucher_sl_no`).val(),
          InvoiceNo: $(`${select} #invoice_no`).val(),
          DebitVoucherNo: $(`${select} #debit_voucher_no`).val(),
        };
        // console.log(voucher_param)
        var s_v_url = base + "post-api/voucher-base-info/";
        var s_v_id = await PurchasePostFunction(s_v_url, voucher_param);
        voucher_ids.push(s_v_id);

        // console.log(select)
        let total_param = {
          total: $(`${select} #main_total`).val(),
          cgst_amount: $(`${select} #cgst_total`).val(),
          sgst_amount: $(`${select} #sgst_total`).val(),
          total_amount: $(`${select} #total_amount`).val(),
          VoucherMaterialInfo: p_id,
          Info: s_v_id,
        };
        // console.log(total_param)
        var total_url = base + "post-api/voucher-amount/";
        var total_id = await PurchasePostFunction(total_url, total_param);
        total_ids.push(total_id);
      }

      var params = {
        VendorId: $("#addvoucher #voucher_name").attr("vendor-id"),
        vendorDetail: voucher_vendor_id,
        quotation: quotation_id,
        amount: total_ids,
        signature: Signature,
      };

      var vd_ids = [];

      var action_url = base + "post-api/voucher-detail/";
      var vd_id = await PurchasePostFunction(action_url, params);
      // // location.reload()
      vd_ids.push(vd_id);

      var voucher_params = {
        quotation: quotation_id,
        voucher: vd_ids,
        purchase: $("#purchaseID").text(),
      };

      var voucher_action_url = base + "post-api/voucher/";
      await PurchasePostFunction(voucher_action_url, voucher_params);
      alert("Voucher Added. !!!");
      location.reload();
    } else {
      alert("voucher date, debit voucher number and signature Cannot Be Empty. !!!");
    }
  });
}

// purchase post function;
function PurchasePostFunction(action_url, data) {
  var data;
  $.ajax({
    type: "POST",
    url: action_url,
    contentType: "application/json",
    dataType: "json",
    async: false,
    data: JSON.stringify(data),
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {
      data = response?.id;
    },
    error: function (response) {
      // console.log(response);
    },
  });
  return data;
}

// purchase patch method
function PurchasePatchMethod(params, dynamicurl) {
  $.ajax({
    type: "PATCH",
    url: dynamicurl,
    data: JSON.stringify(params),
    processData: false,
    contentType: "application/json",
    dataType: "json",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {},
    error: function (response) {
      alert("Network issue Try again later. !!!");
    },
  });
}
