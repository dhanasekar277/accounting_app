$(document).ready(function () {

  // alert('works')
  var ph_data = false;
  var gst_data = false;
  var tin_data = false;
  var pan_data = false;
  var po_ids = [];
  var sales = [];
  var material_name = [];
  var sale_id;
  var salesCount = Number($(".salesCount").text());
  for (var i = 0; i < salesCount; i++) {
    let select = `.sales${i + 1}`;
    var mname = $(`${select} #mname`).text();
    var poid = $(`${select} .poid`).text();
    var params = {
      poid: poid,
      materialName: mname,
      hsnc: $(`${select} #mhsnc`).text(),
      qty: $(`${select} #mqty`).text(),
      qtytype: Enc_QuantityType($(`${select} #mqtype`).text()),
      price: $(`${select} #mprice`).text(),
    };
    sales.push(params);
  }

  $("#material_list .generateInvoice").click(function (e) {
    e.preventDefault();

    var id = $(this).attr("href");
    $(`.invoice_print, .delete_invoice, .invoicePhone, .download_xl, .download_excel`).addClass("d-none");
    $(
      `#InvoiceNo, #InvoiceDate, #DeliveryNote, #OtherReference, #SupplierRef, #TermsPayment, #DespatchDocumentNo, #DeliveryNote, #Destination`
    )
      .removeAttr("disabled")
      .val("");
    $("#phone_data, #bank_account, #invoice_submit").removeClass("d-none");
    sale_id = id;
    var sale_data = GetData(`${base}api/sales/${id}/`);
    // console.log(sale_data)
    var customer_data = sale_data?.customer;
    var order_data = sale_data?.orderid;
    var sales = sale_data?.poInfo;

    // console.log(sale_data)

    $(".company_name").text(customer_data?.customerid?.Company_Name);
    $("#TermsPayment").val(customer_data?.customerid?.Payment_Terms);
    $(".company_address").text(
      `${customer_data?.customerid?.Company_Address},`
    );
    $(".company_city_zip").text(
      `${customer_data?.customerid?.Company_City} - ${customer_data?.customerid?.Company_Zip},`
    );
    $(".company_state_country").text(
      `${customer_data?.customerid?.Company_State}, ${customer_data?.customerid?.Company_Country}`
    );
    $(".company_delivery_address").text(order_data?.Sales_Delivery_Address);
    $(".customer_gst_no").text(customer_data?.gst?.GST_No);
    $(".customer_pan_no").text(customer_data?.pan?.PAN_No);

    //get invoice data
    getInvoice();

    $(".invoice_section").removeClass("d-none");
    $("#salesMaterial").html("");

    var qty = 0;
    var qtytype;
    var total_product_price = 0;
    var split = 0;
    var hsnc = "";
    var gst_percentage;

    po_ids = [];

    for (var i = 0; i < sales.length; i++) {
      var mname = sales[i]?.MatId?.Material_Name;
      var q_type = Enc_QuantityType(sales[i]?.MatId?.Quantity_Type);
      qtytype = q_type;
      gst_percentage = sales[i]?.MatId?.Product_Name?.GST;

      // console.log(mname)
      qty += Number(sales[i]?.qty);
      total_product_price += Number(sales[i]?.Total);
      let obj = material_name.find((o) => o === mname);

      if (obj == undefined) {
        material_name.push(mname);
      }
    }

    for (var i = 0; i < material_name.length; i++) {
      // console.log(material_name[i])
      var data = sales.filter((p) => p.MatId.Material_Name == material_name[i]);
      // console.log("data",data)
      var p_qty = 0;
      var p_total = 0;
      let cdcarr = [];
      let datecarr = [];
      for (var j = 0; j < data.length; j++) {
        p_qty += Number(data[j]?.qty);
        p_total += Number(data[j]?.Total);
        cdcarr.push(data[j]?.CDC);
        datecarr.push(data[j]?.Date);
      }
      // console.log(p_qty)
      var q_type = Enc_QuantityType(data[0]?.MatId?.Quantity_Type);
      // console.log(data[0])
      $("#salesMaterial").append(`<tr class="po${i}">
          <td>${i + 1}</td>
          <td class="material_list"><span class="mname">${data[0]?.MatId?.Material_Name}</span><br>
          <input type="text" placeholder="DC No" value="${cdcarr.join()}" class="dcno" style="width: 200px;">
          <input class="ms-1 dcdate" style="width: 263px;" value="${datecarr.join()}" type="text" placeholder="Date"></td>
          <td><span class="hsnc">${data[0]?.MatId?.HSNCode}</span></td>
          <td><span class="pqty">${p_qty.toFixed(2)}</span> ${q_type}</td>
          <td><span class="rate">${data[0]?.MatId?.Final_Offer_Price
        }</span></td>
          <td><span class="ptype">${q_type}</span></td>
          <td><span class="total">${p_total.toFixed(2)}</span></td>
      </tr>`);
    }

    if (split > 1) {
      $(".total_product_price").removeClass("d-none");
      $("#ttl_price").text(parseFloat(total_product_price).toFixed(2));
    } else {
      $(".total_product_price").addClass("d-none");
      $("#ttl_price").text();
    }

    // gst_percentage = gst_percentage.substring(0, gst_percentage.length - 1);
    gst_percentage = Number(gst_percentage) / 2;
    $(".sgst_cgst_per").text(gst_percentage);
    $(".sgst_cgst_").text(`${gst_percentage}0`);
    gst_percentage = gst_percentage / 100;
    // console.log(gst_percentage)

    $("#total_qtys").html(`${qty.toFixed(2)} ${qtytype}`);
    var cgst = total_product_price * gst_percentage;
    var to_round_off = cgst + cgst;
    to_round_off = String(to_round_off);
    to_round_off = to_round_off.substr(to_round_off.indexOf("."));

    var final_total = total_product_price + cgst + cgst;
    var final_total_price_words = price_in_words(Math.round(final_total));

    $("#total_words").text(final_total_price_words);
    var tax = cgst + cgst;
    $("#tax_words").text(price_in_words(Math.round(tax)));
    $(".cgst_price, .sgst_price").text(parseFloat(cgst).toFixed(2));
    $("#total").text(parseFloat(final_total).toFixed(2));
    $("#rounded_price").text(Number(to_round_off).toFixed(2));
    $("#hsnc").text(hsnc);
    $(".final_total").text(parseFloat(total_product_price).toFixed(2));
    $(".tax").text(parseFloat(tax).toFixed(2));

    selectBank();
    invoiceSubmit();

    invoice_corrections(sale_data?.poInfo)
  });

  $("#material_list .sale_invoice").click(function (e) {
    e.preventDefault();
    var si_id = $(this).attr("href");
    $(`.invoice_print, .delete_invoice, #phone_data, #bank_account, .download_xl, download_excel`).addClass(
      "d-none"
    );
    $(`.ip${si_id}, .id${si_id}, .invoice_section, .invoicePhone `).removeClass(
      "d-none"
    );

    // console.log(si_id)
    var sale_data = GetData(`${base}api/single-invoice/?saleid=${si_id}`);
    // console.log(sale_data)

    var sale_invoice = sale_data?.results[0];
    var sale_invoice_dc = sale_invoice?.DC;
    var sales = sale_invoice?.saleid;
    var customer = sales?.customer;
    // console.log(customer)
    $(".company_name").text(`${customer?.customerid?.Company_Name},`);
    $(".company_address").text(`${customer?.customerid?.Company_Address},`);
    $(".company_city_zip").text(
      `${customer?.customerid?.Company_City} - ${customer?.customerid?.Company_Zip},`
    );
    $(".company_state_country").text(
      `${customer?.customerid?.Company_State}, ${customer?.customerid?.Company_Country}`
    );

    $(".customer_gst_no").text(customer?.gst?.GST_No);
    $(".customer_pan_no").text(customer?.pan?.PAN_No);

    var gst_percentage =
      sale_invoice?.saleid?.poInfo[0]?.MatId?.Product_Name?.GST;
    // console.log(gst_percentage)

    // gst_percentage = gst_percentage.substr(0, gst_percentage.length - 1);
    var cgst_sgst = Number(gst_percentage) / 2;

    // console.log(cgst_sgst)

    var cgst = `${String(cgst_sgst)}0`;
    $(".sgst_cgst_per").text(cgst_sgst);
    $(".sgst_cgst_").text(cgst);

    // console.log(sale_invoice_dc)
    // console.log(sales)
    $("#salesMaterial").html("");

    var total_quantity = 0;
    var total_amount = 0;

    for (var i = 0; i < sale_invoice_dc.length; i++) {
      $("#salesMaterial").append(`<tr class="po${i}">
                <td>${i + 1}</td>
                <td class="material_list"><span class="mname">${sale_invoice_dc[i]?.material_name
        }</span><br>
                <span class="me-1">${sale_invoice_dc[i]?.dcNo
        }</span>/<span class="ms-1">${sale_invoice_dc[i]?.dcdate
        }</span></td>
                <td><span class="hsnc">${sale_invoice_dc[i]?.hsc}</span></td>
                <td><span class="pqty">${sale_invoice_dc[i]?.quantity}</span> ${sale_invoice_dc[i]?.per
        }</td>
                <td><span class="rate">${sale_invoice_dc[i]?.rate}</span></td>
                <td><span class="ptype">${sale_invoice_dc[i]?.per}</span></td>
                <td><span class="total">${Math.round(sale_invoice_dc[i]?.amount)}</span></td>
            </tr>`);

      total_quantity += Number(sale_invoice_dc[i]?.quantity);
      total_amount += Number(Math.round(sale_invoice_dc[i]?.amount));
    }

    cgst_sgst = cgst_sgst / 100;
    cgst_sgst = total_amount * cgst_sgst;
    var round_off = cgst_sgst + cgst_sgst;
    round_off = round_off.toFixed(4);
    round_off = String(round_off);
    round_off = round_off.substr(round_off.indexOf("."));

    total_amount = total_amount + cgst_sgst + cgst_sgst;
    $("#total").text(`${total_amount.toFixed(4)}`);
    total_amount = price_in_words(Math.round(total_amount));
    var tax_words = price_in_words(Math.round(cgst_sgst + cgst_sgst));

    $(".cgst_price, .sgst_price").text(cgst_sgst.toFixed(4));
    $("#rounded_price").text(round_off);
    $("#total_qtys").text(`${total_quantity} ${sale_invoice_dc[0]?.per}`);
    $("#total_words").text(total_amount);
    $(".tax").text(`${(cgst_sgst + cgst_sgst).toFixed(4)}`);
    $("#tax_words").text(tax_words);

    $("#InvoiceNo").val(sale_invoice?.InvoiceNo).attr("disabled", true);
    $("#InvoiceDate").val(sale_invoice?.InvoiceDate).attr("disabled", true);
    $("#DeliveryNote").val(sale_invoice?.DeliveryNote).attr("disabled", true);
    $("#OtherReference")
      .val(sale_invoice?.OtherReference)
      .attr("disabled", true);
    $("#SupplierRef").val(sale_invoice?.SupplierRef).attr("disabled", true);
    $("#TermsPayment").val(sale_invoice?.TermsPayment).attr("disabled", true);
    $("#DespatchDocumentNo")
      .val(sale_invoice?.DespatchDocumentNo)
      .attr("disabled", true);
    $(".delivery_note").val(sale_invoice?.DeliveryNote).attr("disabled", true);
    $("#Destination").val(sale_invoice?.Destination).attr("disabled", true);
    $(".invoicePhone").text(sale_invoice?.phone?.Phone);
    $(".ibank").text(sale_invoice?.BankAccount?.Bank_Name);
    $(".iac_no").text(sale_invoice?.BankAccount?.Account_Number);
    $(".ibranch").text(sale_invoice?.BankAccount?.Branch);
    $(".iifsc").text(sale_invoice?.BankAccount?.IFSC_Code);
    $("#invoice_id").text(sale_invoice?.InvoiceNo);
    $("#date_generated").text(sale_invoice?.InvoiceDate);
    $("#invoice_submit").addClass("d-none");


    // invoice section after 5 entries
    invoice_corrections(sale_data?.results[0]?.saleid?.poInfo)
  });


  function invoice_corrections(data) {
    // console.log(data)
    let po_length = data.length
    if (po_length > 5) {

      const uniques = [...new Set(data.map(item => item?.MatId?.Material_Name))];
      for (i = 0; i < uniques.length; i++) {
        let po_lengths = data.filter(p => p?.MatId?.Material_Name == uniques[i]).length

        $(`.po${i} .material_list`).html(`
          <span class="text-capitalize">${uniques[i]}</span><br>
          <span class="text-uppercase">${po_lengths} LOADS <span class="mn">${uniques[i]}</span> DETAILS ARE <br>ATTACHED IN THE EXCEL SHEET</span>
        `)
      }

    }

  }

  $('.download_excel').click(function (e) {
    e.preventDefault()
    let id = $(this).attr('href')
    let data = GetData(`${base}api/single-invoice/?saleid=${id}`)
    let po = data?.results[0]?.saleid?.poInfo
    let sale_data = data?.results[0]

    material_name = $('.material_list .mn').text()
    // console.log(material_name)
    i_no = sale_data?.DespatchDocumentNo
    po.map(p => delete p['MatId'])
    po.map(p => delete p['Formula'])
    po.map(p => delete p['ig'])
    po.map(p => delete p['orderId'])
    po.map(p => delete p['RoundOff'])
    po.map(p => p['Material'] = material_name)
    filename = `invoice_${i_no}_dc_report.xlsx`;
    data = po
    var ws = XLSX.utils.json_to_sheet(data);
    var wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "DC");
    XLSX.writeFile(wb, filename);
  })


  $('.download_xl').click(function (e) {
    e.preventDefault()
    $('#SummaryModal').modal("show")
    var si_id = $(this).attr("href");
    var sale_data = GetData(`${base}api/single-invoice/?saleid=${si_id}`);
    const agencyDetails = sale_data.results[0].saleid.orderid.Agency
    const poDetails = sale_data.results[0].saleid.poInfo
    const orderDetails = sale_data.results[0].saleid.orderid
    // console.log(orderDetails)

    $("#SummaryModal .modal-body").html(`
    <div id="invoice_summary" >
      <table class="table table-bordered mb-0">
          <tr>
              <td colspan="7" class="text-center fw-bold">EXCEL SHEET (DC WISE DETAILS)</td>
          </tr>
          <tr>
              <td width="30%"><b>GST NO : </b> ${agencyDetails.GST_Number}</td>
              <td width="40%" class="text-center text-uppercase fw-bold h5 text-primary"> ${agencyDetails.Name}</td>
              <td width="30%"><b>PHONE NO : </b>${sale_data.results[0].phone.Phone}</td>
          </tr>
          <tr>
              <td colspan="7" class="text-center w-75">
                  ALL KINDS OF RIVER SAND & TABLE MOULD BRICKS AGRIGATES SUPPLIERS <br>
                  ${agencyDetails.Address}, ${agencyDetails.City}, ${agencyDetails.Zip}, ${agencyDetails.State}, ${agencyDetails.Country} <br>
                  <b>E-mail : </b> ${agencyDetails.Email}
              </td>
          </tr>
      </table>
      <table class="table table-bordered mb-0">
          <tr class="border-top-0">
              <td width="50%">
                  <div class="text-underline text-primary">BILLING ADDRESS</div>
                  <div class="text-underline fw-bold">${orderDetails.Sales_Company.Company_Name}</div>
                  <div class="ms-3">${orderDetails.Billing_Address}</div>
              </td>
              <td>
                  <div class="text-underline text-primary">ULOADING PLACE</div>
                  <div class="text-underline fw-bold">${orderDetails.Sales_Company.Company_Name}</div>
                  <div class="ms-3">${orderDetails.Sales_Delivery_Address}</div>
                  <div class="border-3">
                      <b>PO NO: </b>${orderDetails.PO_Number.PO_Number}
                  </div>
                  <div class="border-3">
                      <b>PO Date: </b>${orderDetails.PO_Number.PO_Date}
                  </div>
              </td>
          </tr>
          <tr>
              <td width="50%">
                  <div class="h6 fw-bold">INV NO : ${sale_data.results[0].InvoiceNo}</div>
              </td>
              <td>
                  <div class="h6 fw-bold">Date : ${sale_data.results[0].InvoiceDate}</div>
              </td>
          </tr>
      </table>
      <table class="table table-bordered mb-0">
          <tr class="border-top-0 bg-warning">
              <th>S.No</th>
              <th>DC DATE</th>
              <th>DC NO</th>
              <th>VEHICLE NO</th>
              <th>MATERIAL</th>
              <th>QUANTITY</th>
              <th>RATE</th>
              <th>AMOUNT</th>
          </tr>
          <tbody class="matdetails"></tbody>
          <tr class="text-light bg-primary">
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>TOTAL QUANTITY</td>
              <td class="tQuantity"></td>
              <td>AMOUNT</td>
              <td class="tAmount"></td>
          </tr>
          <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>TOTAL PO QUANTITY</td>
              <td class="tPoQuantity"></td>
              <td>CGST 2.5%</td>
              <td class="gstAmount"></td>
          </tr>
          <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>SGST 2.5%</td>
              <td class="gstAmount"></td>
          </tr>
          <tr class="text-light bg-success">
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>BALANCE QUANTITY</td>
              <td class="balQuantity"></td>
              <td>TOTAL</td>
              <td class="tAmountgst"></td>
          </tr>
      </table>
      </div>
    `)

    let totalQuantity = 0
    let totalAmount = 0
    let singlegstamount = 0
    let sgst = 0
    let index = 0
    let totalPOQuantity = 0
    for (i of orderDetails.PO_Number.PO_Material_Info) totalPOQuantity += Number(i.Quantity)
    for (i of poDetails) {
      $('.matdetails').append(`
      <tr>
        <td>${index += 1}</td>
        <td>${i.Date}</td>
        <td>${i.CDC}</td>
        <td>${i.VehicleNo}</td>
        <td>${i.MatId.Material_Name}</td>
        <td>${i.qty}</td>
        <td>${i.MatId.Sale_Price}</td>
        <td>${Number(i.Total).toFixed(0)}</td>
      </tr>
      `)
      totalQuantity += Number(i.qty)
      totalAmount += Number(i.Total)
      singlegstamount = (Number(i.Total) * Number(i.MatId.Product_Name.GST)) / 100
      sgst += singlegstamount
    }
    $('.gstAmount').text(Number(sgst / 2).toFixed(0))
    $('.tAmount').text(totalAmount.toFixed(0))
    $('.tAmountgst').text(Number(totalAmount + sgst).toFixed(0))
    $('.tQuantity').text(totalQuantity.toFixed(2))
    $('.tPoQuantity').text(totalPOQuantity.toFixed(2))
    $('.balQuantity').text((totalPOQuantity - totalQuantity < 0) ? 0 : Number(totalPOQuantity - totalQuantity).toFixed(2))
  })


  function getInvoice() {
    var previous_sales_invoice_url = `${base}invoices/get-latest-invoice`;
    var pre_si_data = GetData(previous_sales_invoice_url);
    // console.log(pre_si_data);
    pre_si_data = JSON.parse(pre_si_data);
    var pre_si_data = pre_si_data.length == 0 ? 0 : pre_si_data[0]?.pk;
    // console.log(pre_si_data);
    var now = new Date();
    presentYear = now.getFullYear();
    nextYear = presentYear + 1;
    let gen_invoice_id = `${pre_si_data + 1}/${presentYear}-${nextYear}`;
    // console.log(gen_invoice_id)
    $("#InvoiceNo").val(gen_invoice_id);
    $("#invoice_id").text(gen_invoice_id);
  }

  // select bank
  function selectBank() {
    var id = $("#bank_account").val();
    var acc_url = `${url}agency-bank/${id}/`;
    let bank_data = GetData(acc_url);
    $(".ibank").text(bank_data?.Bank_Name);
    $(".iac_no").text(bank_data?.Account_Number);
    $(".ibranch").text(bank_data?.Branch);
    $(".iifsc").text(bank_data?.IFSC_Code);

    $("#bank_account").change(function (e) {
      e.preventDefault();
      var id = $(this).val();
      var acc_url = `${url}agency-bank/${id}/`;
      let bank_data = GetData(acc_url);
      $(".ibank").text(bank_data?.Bank_Name);
      $(".iac_no").text(bank_data?.Account_Number);
      $(".ibranch").text(bank_data?.Branch);
      $(".iifsc").text(bank_data?.IFSC_Code);
    });
  }

  // invoice submit details
  function invoiceSubmit() {
    $("#invoice_submit").click(async function (e) {
      e.preventDefault();
      var dc_ids = [];
      var dc_url = `${base}post-api/dc-detail/`;
      var single_si_url = `${base}post-api/single-invoice/`;
      var si_url = `${base}post-api/sale-invoice/`;

      var InvoiceDate = $("#InvoiceDate").val();
      var DeliveryNote = $("#DeliveryNote").val();
      var OtherReference = $("#OtherReference").val();
      var SupplierRef = $("#SupplierRef").val();
      var phone_data = $("#phone_data").val();
      var DespatchDocumentNo = $("#DespatchDocumentNo").val();
      var Destination = $("#Destination").val();
      var bank_account = $("#bank_account").val();

      if (
        InvoiceDate == "" ||
        phone_data == "" ||
        DespatchDocumentNo == "" ||
        bank_account == ""
      ) {
        alert(
          "Invoice Date, Phone Number, Despatch Document No, bank account fields are required"
        );
      } else {
        $(this).prop("disabled", true);
        for (var i = 0; i < material_name.length; i++) {
          var dc_params = {
            material_name: $(`.po${i} .mname`).text(),
            dcNo: $(`.po${i} .dcno`).val(),
            dcdate: $(`.po${i} .dcdate`).val(),
            hsc: $(`.po${i} .hsnc`).text(),
            quantity: $(`.po${i} .pqty`).text(),
            rate: $(`.po${i} .rate`).text(),
            per: $(`.po${i} .ptype`).text(),
            amount: $(`.po${i} .total`).text(),
          };
          var dcid = await PostData(dc_params, dc_url);
          dc_ids.push(dcid);
        }

        var $form = $("#invoice_details");
        var fd = getFormData($form);
        // console.log(fd);
        fd["DC"] = dc_ids;
        fd["saleid"] = sale_id;
        fd["orderid"] = $("#orderId").text();
        // console.log(fd);
        var sale_invoice_id = await PostData(fd, single_si_url);

        var sale_invoice_params = {
          sale_invoice: true,
        };
        await PatchMethod(
          sale_invoice_params,
          `${base}post-api/sales/${sale_id}/`
        );
        var sale_data_id = $("#saleId").text();
        var sale_invoice_data_check = GetData(
          `${base}post-api/sale-invoice/?saleid=${sale_data_id}`
        );

        if (sale_invoice_data_check?.count > 0) {
          // console.log('do update')
          var invoice = sale_invoice_data_check?.results[0]?.invoice;
          invoice.push(sale_invoice_id);
          var si_params = {
            invoice: invoice,
          };
          var si_url = `${base}post-api/sale-invoice/${sale_invoice_data_check?.results[0]?.id}/`;
          await PatchMethod(si_params, si_url);
          alert("Sales Invoice Generated Successfully. !!!");
        } else {
          // console.log('do add')
          var si_params = {
            saleid: $("#saleId").text(),
            invoice: [sale_invoice_id],
          };
          var si_id = await PostData(si_params, si_url);
          alert("Sales Invoice Generated Successfully. !!!");
        }

        location.reload();
      }
    });
  }

  function getFormData($form) {
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};
    $.map(unindexed_array, function (n, i) {
      indexed_array[n["name"]] = n["value"];
    });
    return indexed_array;
  }

  // price in words
  function price_in_words(price) {
    var sglDigit = [
      "Zero",
      "One",
      "Two",
      "Three",
      "Four",
      "Five",
      "Six",
      "Seven",
      "Eight",
      "Nine",
    ],
      dblDigit = [
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
      ],
      tensPlace = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
      ],
      handle_tens = function (dgt, prevDgt) {
        return 0 == dgt
          ? ""
          : " " + (1 == dgt ? dblDigit[prevDgt] : tensPlace[dgt]);
      },
      handle_utlc = function (dgt, nxtDgt, denom) {
        return (
          (0 != dgt && 1 != nxtDgt ? " " + sglDigit[dgt] : "") +
          (0 != nxtDgt || dgt > 0 ? " " + denom : "")
        );
      };

    var str = "",
      digitIdx = 0,
      digit = 0,
      nxtDigit = 0,
      words = [];
    if (((price += ""), isNaN(parseInt(price)))) str = "";
    else if (parseInt(price) > 0 && price.length <= 10) {
      for (digitIdx = price.length - 1; digitIdx >= 0; digitIdx--)
        switch (
        ((digit = price[digitIdx] - 0),
          (nxtDigit = digitIdx > 0 ? price[digitIdx - 1] - 0 : 0),
          price.length - digitIdx - 1)
        ) {
          case 0:
            words.push(handle_utlc(digit, nxtDigit, ""));
            break;
          case 1:
            words.push(handle_tens(digit, price[digitIdx + 1]));
            break;
          case 2:
            words.push(
              0 != digit
                ? " " +
                sglDigit[digit] +
                " Hundred" +
                (0 != price[digitIdx + 1] && 0 != price[digitIdx + 2]
                  ? " and"
                  : "")
                : ""
            );
            break;
          case 3:
            words.push(handle_utlc(digit, nxtDigit, "Thousand"));
            break;
          case 4:
            words.push(handle_tens(digit, price[digitIdx + 1]));
            break;
          case 5:
            words.push(handle_utlc(digit, nxtDigit, "Lakh"));
            break;
          case 6:
            words.push(handle_tens(digit, price[digitIdx + 1]));
            break;
          case 7:
            words.push(handle_utlc(digit, nxtDigit, "Crore"));
            break;
          case 8:
            words.push(handle_tens(digit, price[digitIdx + 1]));
            break;
          case 9:
            words.push(
              0 != digit
                ? " " +
                sglDigit[digit] +
                " Hundred" +
                (0 != price[digitIdx + 1] || 0 != price[digitIdx + 2]
                  ? " and"
                  : " Crore")
                : ""
            );
        }
      str = words.reverse().join("");
    } else str = "";
    return str;
  }

  // quantity type formulas
  function QuantityFormula(type, qty) {
    // mt formula
    if (type == "MT") {
      // console.log(Number(qty));
      // console.log(Number(qty) * 1000);
      return Number(qty) * 1000;
    }
    // cft formula
    else if (type == "CFT") {
    }
  }
});
