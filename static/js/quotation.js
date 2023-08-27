var quotation = document.getElementById("quotation");
var csrftoken = $('meta[name="csrf-token"]').attr("content");
quotation.addEventListener("show.bs.modal", function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget;
  // Extract info from data-bs-* attributes
  var quotation = button.getAttribute("data-id");
});

var quotation_id;
function DeleteForUser(_id, _url, _method) {
  if (confirm("Are you sure you want to delete?")) {
    var user = $("#user_name").attr("data-name");
    let person = prompt("Please enter your name ?");
    if (person == user) {
      let id = _id;
      let action_url = _url;
      var base = window.location.protocol + "//" + window.location.host + "/";
      var url = base + "api/";
      let active_action_url = `${url}${action_url}/${id}/`;

      var params = {
        is_active: false,
      };
      PatchMethod(params, active_action_url);
      var _obj = JSON.stringify({ id: id, model: action_url });
      // console.log(_obj)

      var params = {
        Notifications: _obj,
        csrfmiddlewaretoken: csrftoken,
        Types: _method,
        User: $("#userid").html(),
      };

      $.post(base + "post-api/notifications/", params, function (req, res) {
        alert("Delete Request sended successfully. !!!");
        location.reload();
      });
    } else {
      alert("Invalid Name. !!!");
    }
  }
}

function QuotationPostData(params, action_url) {
  var data;
  $.ajax({
    type: "POST",
    url: action_url,
    contentType: "application/json",
    dataType: "json",
    async: false,
    data: JSON.stringify(params),
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {
      data = response?.id;
      callback.call(data);
    },

    error: function (response) {
      alert("Network Error. !!!");
    },
  });
  return data;
}

function PostData(params, action_url) {
  var data;
  $.ajax({
    type: "POST",
    url: action_url,
    contentType: "application/json",
    dataType: "json",
    async: false,
    data: JSON.stringify(params),
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {
      data = response?.id;
      callback.call(data);
    },

    error: function (response) {
      alert("Network Error. !!!");
    },
  });
  return data;
}

function PostFormSubmit(Formdata, action_url) {
  var data;
  $.ajax({
    url: action_url,
    type: "POST",
    data: Formdata,
    async: false,
    success: function (response) {
      data = response?.id;
    },
    headers: {
      "X-CSRFToken": csrftoken,
    },
    cache: false,
    contentType: false,
    processData: false,
  });
  return data;
}

// purchase patch method
function PatchMethod(params, dynamicurl) {
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

function DeleteMethod(params, _url) {
  let person = prompt("Please Enter Your Name ?", "");
  var user_name = $("#user_name").attr("data-name");
  if (person == user_name) {
    $.ajax({
      type: "DELETE",
      url: _url,
      contentType: "application/json",
      dataType: "json",
      data: JSON.stringify(params),
      headers: {
        "X-CSRFToken": csrftoken,
      },
      success: function (response) {
        alert("Deleted Successfully. !!!");
        location.reload();
      },
    });
  } else {
    alert("Invalid Username. !!!");
  }
}
function DeleteWithOutValidation(params, _url) {
  $.ajax({
    type: "DELETE",
    url: _url,
    contentType: "application/json",
    dataType: "json",
    data: JSON.stringify(params),
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {},
  });
}
function QuotationPatchData(params, actionurl) {
  // console.log(params);
  // console.log(actionurl);
  $.ajax({
    type: "PATCH",
    url: actionurl,
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

// quotation view by usign order id
function QuotationView(id) {
  $("#quotation").modal("toggle");
  var action_url = url + "quotations/" + id + "/";
  quotation_id = id;
  var quotation = GetData(action_url);

  // to generate sales quotation
  // console.log(quotation)
  GenerateSalesQuotation(
    quotation?.sales,
    quotation?.purchase?.material,
    quotation?.order,
    quotation?.customerGenerate,
    quotation?.id,
    quotation?.customerInfo,
    quotation
  );
  GenerateVendorQuotation(quotation);
}

// to generate sales Quotations functions (customer)
function GenerateSalesQuotation(
  sales,
  materials,
  order,
  generate,
  id,
  customerinfo,
  quotation
) {
  const customer = sales?.customer;
  const po = sales?.po;
  const po_materials = sales?.po_materials;
  const quo_id = id;
  // console.log(materials)

  var hsc_code = materials.map((p) => p.HSNCode);
  let hsc_obj = hsc_code.filter(
    (v, i, a) =>
      a.findIndex((t) => JSON.stringify(t) === JSON.stringify(v)) === i
  );
  // console.log(customerinfo);
  if (customerinfo != null) {
    //do do
    var cf = customerinfo;
    $("#customer_quotation_date").html(`<b>Date : </b> ${cf?.generateDate}`);

    // console.log(cf)
    $(".othertermGST").remove();
    $(".otherterms").html("");
    if (cf?.gstType == "Including GST") {
      $(".otherterms").append(`
            <ul>
                <li>All Price and include GST.</li>
                <li class="my-1">Quotations ${cf?.days} count. </li>
                <li>Advanced amount ${cf?.advance}. </li>
            </ul>
            `);
    } else {
      $(".otherterms").append(cf?.NonGstTerms);
      ckEditor("customer_terms_editor");
    }
  } else {
    $("#customer_quotation_date").html(
      `<b>Date : </b><input type="date" id="quotation_generate" class="border-0 border-bottom"/>`
    );
  }

  var checkDisable = generate == true ? "disabled" : "";
  var checkClass = generate == true ? "border-0" : "border-0 border-bottom";

  $("#customerQuotation").html("");
  // customer po details genereate
  for (let i = 0; i < po_materials.length; i++) {
    $("#customerQuotation").append(`
        <tr>
            <td>${po_materials[i]?.Material_Name}</td>
            <td>${hsc_obj[i]}</td>
            <td>${po_materials[i]?.Quantity} ${po_materials[i]?.Quantity_Type}</td>
            <td>Rs. ${po_materials[i]?.PO_Rate}</td>
            <td>AT SITE</td>
        </tr>
        `);
  }
  // customer info append
  $("#quotation_customer_info").html(`
        <b>TO ,</b>
        <div class="text-capitalize mb-1"><input type="text" id="f_name" ${checkDisable} class="${checkClass}" value="Mr/Mrs. ${customer?.Founder_Name}"></div>
        <div class="text-capitalize mb-1"><input type="text" id="f_position" ${checkDisable} class="${checkClass}" value="Purchase Head"/></div>
        <div class="text-capitalize mb-1"><input type="text" id="f_company" ${checkDisable} class="${checkClass}" value="${customer?.Company_Name}"/></div>
        <div class="text-capitalize mb-1"><input type="text" id="f_address" ${checkDisable} class="${checkClass} w-50" value="${customer?.Company_Address}, ${customer?.Company_City} - ${customer?.Company_Zip}, ${customer?.Company_State}, ${customer?.Company_Country}"/></div>
    `);

  if (generate == false) {
    $(".action_button").html(
      `<button class="btn btn-primary generateQuotation">Generate Quotation</button>`
    );
    // generate quotation
    FinalGenerateQuotation(quo_id, quotation);
  } else {
    // print quotation
    $(".action_button").html(
      `<button class="btn btn-danger quotationPrint">Print</button>`
    );
    // FinalPrintQuotation('quotationprintdiv')
    GenerateVendorQuotation(quotation);
    onclickprint();
  }
}

// generate quotation functionality
function FinalGenerateQuotation(id, quotation) {
  $(".generateQuotation").click(async function () {
    var generate_date = $("#quotation_generate").val();

    var gstcheck = $("#GstCheck").val();
    if (generate_date == "") {
      alert("Quotation Date cannot be empty. !!!");
    }
    if (gstcheck == "") {
      alert("Terms cannot be empty. !!!");
    } else if (gstcheck == "0") {
      let nonGstTerms = myeditor.getData();
      console.log(nonGstTerms);
      if (nonGstTerms) {
        var GstType = $("#GstCheck").val() == 0 ? "Plus GST" : "Including GST";
        var customer_quo_detail = {
          customerName: $("#f_name").val(),
          customerPosition: $("#f_position").val(),
          customerCompany: $("#f_company").val(),
          customerAddress: $("#f_address").val(),
        };
        var quo_detail_url = `${base}post-api/quotation-detail/`;
        var cu_quo_id = await QuotationPostData(
          customer_quo_detail,
          quo_detail_url
        );

        var term_params = {
          detail: cu_quo_id,
          gstType: GstType,
          NonGstTerms: nonGstTerms,
          generateDate: generate_date,
        };
        var quo_terms_url = `${base}post-api/quotation-term/`;
        var cu_quo_id = await QuotationPostData(term_params, quo_terms_url);

        // console.log(customer_quo_detail);

        var infos = {
          customerInfo: cu_quo_id,
          customerGenerate: true,
        };

        var action_url = base + "post-api/quotations/" + id + "/";
        QuotationPatchData(infos, action_url);
        alert("Customer Quotation Generated Successfully. !!!");
        $('a[href="#menu1"], #menu1').addClass("active").removeClass("fade");
        $('a[href="#home"]')
          .attr("disabled", true)
          .removeClass("active")
          .addClass("bg-light");
        $(".tab-content #home").removeClass("active");
        GenerateVendorQuotation(quotation);
      } else {
        alert("Plus GST Terms and Conditions are Empty !!!");
      }
    } else if (generate_date != "" && gstcheck != "") {
      var days = $(".quotationdays").val();
      var advance = $(".quotationadvance").val();
      var GstType = $("#GstCheck").val() == 0 ? "Plus GST" : "Including GST";

      if (days == "" && advance == "") {
        alert("Days & Advance cannot be empty. !!!");
      } else {
        var customer_quo_detail = {
          customerName: $("#f_name").val(),
          customerPosition: $("#f_position").val(),
          customerCompany: $("#f_company").val(),
          customerAddress: $("#f_address").val(),
        };
        var quo_detail_url = `${base}post-api/quotation-detail/`;
        var cu_quo_id = await QuotationPostData(
          customer_quo_detail,
          quo_detail_url
        );

        var term_params = {
          detail: cu_quo_id,
          days: days,
          advance: advance,
          gstType: GstType,
          generateDate: generate_date,
        };
        var quo_terms_url = `${base}post-api/quotation-term/`;
        var cu_quo_id = await QuotationPostData(term_params, quo_terms_url);

        // console.log(customer_quo_detail);

        var infos = {
          customerInfo: cu_quo_id,
          customerGenerate: true,
        };

        var action_url = base + "post-api/quotations/" + id + "/";
        QuotationPatchData(infos, action_url);
        alert("Customer Quotation Generated Successfully. !!!");
        $('a[href="#menu1"], #menu1').addClass("active").removeClass("fade");
        $('a[href="#home"]')
          .attr("disabled", true)
          .removeClass("active")
          .addClass("bg-light");
        $(".tab-content #home").removeClass("active");
        GenerateVendorQuotation(quotation);
      }
    }
  });
}

// print functionality
function FinalPrintQuotation(divName) {
  var printContents = document.getElementById(divName).innerHTML;
  var originalContents = document.body.innerHTML;

  document.body.innerHTML = printContents;

  window.print();

  document.body.innerHTML = originalContents;
}
window.onafterprint = function () {
  window.location.reload();
};

function onclickprint() {
  $(".quotationPrint").click(function (e) {
    e.preventDefault();
    FinalPrintQuotation("quotationprintdiv");
  });
}

var vendor_next = 0;
function GenerateVendorQuotation(quotation) {
  var materials = quotation?.purchase?.material;
  // console.log(quotation)
  var vendor_quotation_list = [];

  var vendor_id = [];

  for (var i = 0; i < materials.length; i++) {
    // console.log(materials[i])
    vendor_id.push(materials[i]?.Vendor?.id);
    vendor_quotation_list.push({
      Material_Name: materials[i]?.Material_Name,
      Quantity: materials[i]?.Quantity,
      Quantity_Type: materials[i]?.Quantity_Type,
      Final_Purchase_Price: materials[i]?.Final_Purchase_Price,
      HSNCode: materials[i]?.HSNCode,
      vendor: materials[i]?.Vendor?.id,
      vendor_detail: materials[i]?.Vendor,
      mat_id: materials[i]?.id,
    });
  }

  // remove duplicates from vendor object
  var unique_vendor = vendor_id.filter((data, index) => {
    return vendor_id.indexOf(data) === index;
  });
  // console.log(unique_vendor)
  v_quo = [];
  // console.log(vendor_quotation_list)
  for (var i = 0; i < unique_vendor.length; i++) {
    var quo = vendor_quotation_list.filter((p) => p.vendor == unique_vendor[i]);
    // console.log(quo)
    v_quo.push(quo);
  }

  // console.log(v_quo)

  GenerateVendor(
    vendor_next,
    v_quo,
    quotation?.vendorGenerate,
    quotation?.vendorInfo,
  );
}
// Vendor Quotation
let vendoreditor;
function GenerateVendor(next, v_quo, vendor_generate_status, vendor_date) {
  var className;
  var tag;

  // console.log(v_quo);

  if (Number(next) > v_quo.length - 2) {
    className = "btn-danger closeVendor";
    tag = "Close";
  } else {
    className = "btn-primary nextVendor";
    tag = "Next";
  }

  var v_q = v_quo[next];
  // console.log(v_q)

  if (vendor_generate_status == true) {
    $(".vendor_quotation").html(`
            <div id="ExampleControls" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner" id="carousel_append">
                    
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#ExampleControls" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#ExampleControls" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        
        `);

    var v_date = vendor_date;
    // console.log(v_date)

    for (var i = 0; i < v_quo.length; i++) {
      var v_q = v_quo[i];
      // console.log(v_q)
      // console.log(v_q);
      var active = i == 0 ? "active" : "";
      // <ol>
      //   <li>SGST (extra) will be applicable & CGST (extra) will be applicable.</li>
      //   <li>The quotation is valied for 7 days only.</li>
      //   <li>Payment within 30 days credit limit from the date of billing.</li>
      //   <li>Check the quality and quantity of material before unloading , at time and issue the material receipt or delivery note at site.</li>
      //   <li>All disputes subject to chennai jurisdiction only.</li>
      // </ol>
      $("#carousel_append").append(`
            <div class="carousel-item ${active}">
            <div class="letterpadheader"></div>
                <div class="float-end date" >
                    <b>Date : </b> <span>${v_date[i]?.date}</span>
                </div>

                <div class="to_address text-captailize">
                    <b>TO ,</b>
                    <div>Mr/Mrs. ${v_q[0]?.vendor_detail?.Vendor_Name}</div>
                    <div>${v_q[0]?.vendor_detail?.Company_Name}</div>
                    <div>${v_q[0]?.vendor_detail?.Address}, ${v_q[0]?.vendor_detail?.City} - ${v_q[0]?.vendor_detail?.Zip}, ${v_q[0]?.vendor_detail?.State}, ${v_q[0]?.vendor_detail?.Country}</div>
                </div>
                <div class="mt-3">
                    <b>Subject : </b> <span>QUOTATION for your enquiry for supply of building basic material.</span>
                </div>
                <div class="mt-2">
                    <b>Dear Sir ,</b>
                    <div>We are pleased to provide following quote of various material requirements for your site.</div>
                </div>
                <table class="table table-bordered mt-3 mb-0">
                    <thead>
                        <tr>
                            <th>MATERIAL</th>
                            <th>HSN CODE</th>
                            <th>QUANTITY</th>
                            <th>RATE</th>
                            <th>DELIVERY</th>
                        </tr>
                    </thead>
                    <tbody id="vendor_material${v_q[0]?.mat_id}">
                        
                    </tbody>
                </table>
                <div class="mt-3">
                    <b class="mb-2">Other terms and conditions</b>
                    ${v_date[i]?.VendorGstTerms}
                </div>
                
                <div class="mt-5 text-end">
                    Thank You,
                    <div class="my-4"></div>
                </div>
                <div class="letterpadfooter">
                                                
                </div>
                <div class="text-center">
                    <button class="btn btn-danger quotationPrint" id="">Print <i class=" me-2 fa fa-print"></i></button>
                </div>
            </div>
            `);
      ckEditor("venorothertrems");
      onclickprint();
      var mat_app_data = v_quo[i];
      for (var j = 0; j < mat_app_data.length; j++) {
        $(`#vendor_material${v_q[0]?.mat_id}`).append(`
                <tr>
                    <td>${mat_app_data[j]?.Material_Name}</td>
                    <td>${mat_app_data[j]?.HSNCode}</td>
                    <td>${mat_app_data[j]?.Quantity} ${Enc_QuantityType(mat_app_data[j]?.Quantity_Type)}</td>
                    <td>Rs. ${mat_app_data[j]?.Final_Purchase_Price}</td>
                    <td>AT SITE</td>
                </tr>
                `);
      }
    }
  } else {
    // if vendor not generated
    $(".vendor_quotation").html(`

            <div class="float-end date" >
                <b>Date : </b><span><input type="date" id="vendor_date${next}"></span>
            </div>

            <div class="to_address text-captailize">
                <b>TO ,</b>
                <div>Mr/Mrs. ${v_q[0]?.vendor_detail?.Vendor_Name}</div>
                <div>${v_q[0]?.vendor_detail?.Company_Name}</div>
                <div>${v_q[0]?.vendor_detail?.Address}, ${
      v_q[0]?.vendor_detail?.City
    } - ${v_q[0]?.vendor_detail?.Zip}, ${v_q[0]?.vendor_detail?.State}, ${
      v_q[0]?.vendor_detail?.Country
    }</div>
            </div>

            <div class="mt-3">
                <b>Subject : </b> <span>QUOTATION for your enquiry for supply of building basic material.</span>
            </div>

            <div class="mt-2">
                <b>Dear Sir ,</b>
                <div>We are pleased to provide following quote of various material requirements for your site.</div>
            </div>

            <table class="table table-bordered mt-3 mb-0">
                <thead>
                    <tr>
                        <th>MATERIAL</th>
                        <th>HSN CODE</th>
                        <th>QUANTITY</th>
                        <th>RATE</th>
                        <th>DELIVERY</th>
                    </tr>
                </thead>
                <tbody id="vendor_material">
                    
                </tbody>
            </table>

            <div class="mt-3">
                <b>Other terms and conditions</b>
                <textarea id="venorothertrems"></textarea>
            </div>

            <div class="mt-5 text-end">
                Thank You,
                <div class="my-4"></div>
            </div>

            <div class="text-center">
                <button class="btn ${className}" id="${
      Number(next) + 1
    }">${tag}<i class=" me-2 fa fa-right"></button>
            </div>
    
        `);
    ClassicEditor.create(document.querySelector(`#venorothertrems`))
      .then((editor) => {
        // console.log(editor);
        vendoreditor = editor;
      })
      .catch((error) => {
        // console.error(error);
      });
  }

  for (var i = 0; i < v_q.length; i++) {
    // console.log(v_q[i])
    $("#vendor_material").append(`
            <tr>
                <td>${v_q[i]?.Material_Name}</td>
                <td>${v_q[i]?.HSNCode}</td>
                    <td>${v_q[j]?.Quantity} ${Enc_QuantityType(v_q[j]?.Quantity_Type)}</td>
                <td>Rs. ${v_q[i]?.Final_Purchase_Price}</td>
                <td>AT SITE</td>
            </tr>
        `);
  }

  NextVendor(v_quo);
}

var vendor_quotation = [];
var quotation_ven_mat_id = [];

function NextVendor(quo) {
  // console.log(quo)
  // next vendor
  $(".nextVendor").click(function (e) {
    e.preventDefault();
    var next_ = $(this).attr("id");
    var dec = Number(next_) - 1;
    var v_date = "#vendor_date" + dec;
    var v_d = $(v_date).val();
    if (v_d == "") {
      alert("Quotation Date is Empty. !!!");
    } else {
      var q = quo[dec];
      var id_ = q.map((p) => p.mat_id);
      var params = {
        date: v_d,
        mat_id: id_,
      };
      // console.log(params);
      vendor_quotation.push(params);
      GenerateVendor(next_, quo);
    }
  });

  // close vendor
  $(".closeVendor").click(async function (e) {
    e.preventDefault();
    var next_ = $(this).attr("id");
    var dec = Number(next_) - 1;
    var v_date = "#vendor_date" + dec;
    var v_d = $(v_date).val();
    let terms = vendoreditor.getData();
    console.log(terms);
    if (v_d == "") {
      alert("Quotation Date is Empty. !!!");
    } else {
      if (!terms) {
        alert("Terms and Conditions Cannot be Empty !!!");
      } else {
        var q = quo[dec];
        // console.log(q)
        var id_ = q.map((p) => p.mat_id);

        var ven_quo_url = `${base}post-api/quotation-vendor-detail/`;
        var params = {
          date: v_d,
          mat_id: id_,
          VendorGstTerms: terms,
        };
        vendor_quotation.push(params);
        // console.log(vendor_quotation)

        vendor_quotation.forEach((p) => {
          var id = QuotationPostData(p, ven_quo_url);
          // console.log(id);
          quotation_ven_mat_id.push(id);
        });

        var data = {
          vendorGenerate: true,
          vendorInfo: quotation_ven_mat_id,
        };
        // console.log(data);
        var action_url = base + "post-api/quotations/" + quotation_id + "/";
        QuotationPatchData(data, action_url);
        // $('#quotation .modal-body').html(`
        // <h2 class="text-center fw-bold py-4 px-3">
        //     Quotation Generated Successfully. !!!
        // </h2>`)
        alert("Quotation Generated Successfully. !!!");

        location.reload();
      }
    }
  });
}

// Note the async keyword
function GetData(dynamic_url) {
  var data;
  $("#preLoader").removeAttr("hidden");
  $.ajax({
    url: dynamic_url,
    type: "GET",
    async: false,
    // beforeSend: function(){

    // },
    success: function (response) {
      data = response;
      // callback.call(data)
    },
    complete: function () {
      $("#preLoader").attr("hidden", true);
    },
    error: function (request, error) {
      data = request?.responseJSON;
    },
    cache: false,
    contentType: false,
    processData: false,
  });

  return data;
}

// gst or including gst check
{
  /* <ul>
<li>System extra will be applicable & CGST extra will be applicable</li>
<li>10,000 Advance Provide before delivery.</li>
</ul> */
}
$("#GstCheck").change(function (e) {
  let gst = $(this).val();
  if (gst == 0) {
    $(".otherterms").html(`
            <textarea id="customer_terms_editor"></textarea>
        `);
    ckEditor("customer_terms_editor");
  } else {
    $(".otherterms").html(`
            <ul>
                <li>All Price and include GST.</li>
                <li class="my-1">Quotations <input type="text" placeholder="Days" class="border-0 quotationdays border-bottom" style="width:10%;" /> count. </li>
                <li>Advanced amount <input type="text" placeholder="Price" class="border-0 quotationadvance border-bottom" style="width:10%;" />. </li>
            </ul>
        `);
  }
});

$("#OtherTermCheck").click(function () {
  var data = $("#GstCheck").val();
  if (data != "") {
    $(".othertermGST").addClass("d-none");
  } else {
    alert("Terms cannot be empty. !!!");
  }
});

// Quotation.html page progress starts here
// get all quotation for quotation.html
function quotation_view(page) {
  var action_url = url + "quotations/?page=" + page;
  var data = GetData(action_url);

  var result = data.results;
  var next = data.next;
  var previous = data.previous;
  var count = data.count;

  for (var i = 0; i < result.length; i++) {
    // console.log(result[i])
    let customer_gen = result[i]?.customerGenerate;
    let vendor_gen = result[i]?.vendorGenerate;
    // sales started
    let customer = result[i]?.sales?.customer;
    let sales = result[i]?.sales?.po_materials;
    // get order
    let po = result[i]?.order?.PO_Number;
    let po_type =
      result[i]?.order?.PO_Number?.PO_Type == "NA"
        ? `<b>PO Not Applicable</b>`
        : `<b>PO Number : </b><span>${po?.PO_Number}</span>`;

    let order = result[i]?.order;
    // console.log(order)
    // purchase started
    let purchase = result[i]?.purchase;
    let purchase_material = purchase?.material;
    // quotation admin approval check
    // check user is administrative
    let admin = $("#permission").attr("admin");

    // console.log(result[i])

    $("#quotation_tbl").append(`
            <tr>
                <td>
                    <div>
                        <b>Sales : </b> <span class="text-capitalize ">${
                          customer?.Founder_Name
                        }</span> 
                        <a href="" class="ms-2 text-success customer_phone"><i class="fa fa-phone"></i></a> 
                        <a href="mailto:${
                          customer?.Founder_Email
                        }" class="ms-2"><i class="fa fa-envelope"></i></a>
                        ${sales_check(customer_gen, result[i]?.id, order)}
                    <br>
                        <span class="text-capitalize ">( ${
                          customer?.Company_Name
                        } )</span>
                    </div>
                    <div class="text-capitalize ">
                        <b>Billing : </b> ${order?.Billing_Address}
                    </div>
                    <div>
                        ${po_type}
                    </div>
                    <ul class="mb-0 ps-3 quotation${
                      result[i]?.id
                    }" style="overflow-y: auto;max-height: 6rem;"></ul>
                </td>
                <td>
                    <ul class="mb-0 ps-3 purchase_quotation${result[i]?.id}">

                        ${purchaseMaterial(
                          purchase_material,
                          result[i]?.vendorInfo,
                          vendor_gen,
                          customer,
                          purchase,
                          result[i]?.id
                        )}
                    </ul>
                </td>
                <td>
                    <div class="mb-0 quota${result[i]?.id}">
                        ${GetQuotationQuantityCounter(
                          purchase?.material,
                          result[i]?.id
                        )}   
                    </div>
                </td>
                <td>
                    <a href="" data-bs-toggle="modal" data-bs-target="#customer_quo"><i class="fa fa-edit"></i></a>
                    <a href="" class="ms-2" data-bs-toggle="modal" data-bs-target="#vendor_quo"><i class="fa fa-trash"></i></a>
                </td> 
            </tr>
        `);

    // purchase quotation

    // console.log(purchase_material)

    // for(var j=0;j<purchase_material.length;j++){
    //     $(`.purchase_quotation${result[i]?.id}`).append(`
    //     <li class="mb-1">
    //         <a href="" data-bs-toggle="modal" data-bs-target="#staticBackdrop">${purchase_material[j]?.Vendor?.Vendor_Name}</a>
    //         ${purchase_check(vendor_gen, purchase_material[i], result[i]?.id, purchase_material)}
    //     </li>
    //     `)
    // }

    // console.log(sales)
    for (var j = 0; j < sales.length; j++) {
      // console.log(sales[i])
      $(`.quotation${result[i]?.id}`).append(`
            <li class="mb-1">
                ${sales[j]?.Material_Name} - ${sales[j]?.Quantity}
            </li>
            `);
    }
  }
}

function purchaseMaterial(data, vendorInfo, check, customer, purchase, id) {
  // console.log(purchase)
  var customer_name = customer?.Founder_Name;
  var company_name = customer?.Company_Name;
  var email = customer?.Founder_Email;
  var address = `${customer?.Company_Address}, ${customer?.Company_Company_City} - ${customer?.Company_Zip}, ${customer?.Company_State}, ${customer?.Company_Country}`;
  // console.log(data)
  if (check == true) {
    if (vendorInfo) {
      // console.log(data)
      var v_json = vendorInfo;
      // console.log(v_json)
      var d = v_json.map((p) => p.mat_id);
      // console.log(d)
      var vendor_info = [];
      for (var i = 0; i < d.length; i++) {
        var material_id = d[i];
        var vendor_mat = [];
        for (var j = 0; j < material_id.length; j++) {
          var m_id = material_id[j];
          var filter_from_data = data.filter((p) => p.id == m_id);
          if (filter_from_data) {
            vendor_mat.push(filter_from_data[0]);
          }
        }
        vendor_info.push(vendor_mat);
      }

      var vendor_final_information = "";
      for (var i = 0; i < vendor_info.length; i++) {
        // console.log(vendor_info[i])
        // console.log(vendor_info[i]);
        var purchase_checks = vendor_info[i].map((p) => p.Purchase_Entry);
        // console.log(purchase_checks)
        // console.log(d[i])

        if (purchase_checks[0] == true) {
          vendor_final_information += `
                    <li class="mb-2">${vendor_info[i][0]?.Vendor?.Company_Name} 
                        <div class="btn-group btn-sm" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-sm py-0 px-1 btn-success" quotation-id="${id}" mat-data="${d[i]}"  data-bs-toggle="modal" data-bs-target="#update_purchase_entry"><i class="fa fa-check fa-12"></i> <small>Purchase</small></button>
                            <button type="button" class="btn btn-sm py-0 px-1 btn-outline-danger" quotation-id="${id}" mat-data="${d[i]}"  data-bs-toggle="modal" data-bs-target="#addvoucher"><i class="fa fa-plus fa-12"></i> <small>Voucher</small></button>
                        </div>
                    </li>`;
        } else {
          vendor_final_information += `
                    <li class="mb-2">${vendor_info[i][0]?.Vendor?.Company_Name} 
                        <a href="" quotation-id="${id}" 
                        mat-data="${d[i]}" 
                        class="btn btn-outline-success py-0 btn-sm ms-1 px-1" data-bs-toggle="modal" data-bs-target="#purchaseEntry"><i class="fa fa-plus fa-12"></i> <small>Purchase</small></a>
                    </li>`;
        }
      }
      return vendor_final_information;
    }
  } else {
    return `Not Approved.`;
  }
}

function sales_check(check, id, order) {
  // console.log(order)
  if (check == true) {
    if (order?.SalesApproved == true) {
      return `<a href="../sales/sales-view/${order?.id}" sales-id=${id} class="float-end btn btn-blue text-white btn-sm py-0 fa-12 SaleEntry" ><i class="fa fa-check"></i> Sales Entry</a>`;
    } else {
      // data-bs-toggle="modal" data-bs-target="#SalesEntryView"
      return `<a href="../sales/sales-entry/${order?.id}" sales-id=${id} class="float-end btn btn-outline-primary btn-sm py-0 fa-12 SaleEntry" ><i class="fa fa-plus"></i> Sales Entry</a>`;
    }
  } else {
    return `<a href="" class="float-end btn btn-danger btn-sm py-0 quotation_view" data-id="${id}" data-bs-toggle="modal" data-bs-target="#quotation_view">Not Approved</a>`;
  }
}

// purchase check
function purchase_check(check, data, id) {
  // console.log(data)
  if (check == true) {
    return `<a href="" class="btn btn-sm btn-outline-primary py-0 px-1 ms-1" data-bs-toggle="modal" data-bs-target="#purchaseEntry" 
        vendor-name="${data?.Vendor?.Vendor_Name}" 
        vendor-id="${data?.Vendor?.id}" 
        purchase-id = "${data?.id}"
        data-id="${id}"><i class="fa fa-plus fa-10 "></i> <small>Purchase</small></a>`;
  } else {
    return `<a href="" class="float-end btn btn-danger btn-sm py-0">Not Approved</a>`;
  }
}

// quotation admin
function GetQuotationQuantityCounter(datas, id) {
  var d = GetQuantityCounter(datas);
  var selector = ".quota" + id;

  var result = "";
  for (var i = 0; i < d.length; i++) {
    var material_name = d[i]?.mat_name;
    result += `<div>${material_name} ( ${d[i]?.total} - ${d[i]?.qty} = ${d[i]?.pending} ) </div>`;
  }
  return result;
}

// get quantity counter data
function GetQuantityCounter(data) {
  var mat_pos = [];
  var material_datas = [];
  for (var i = 0; i < data.length; i++) {
    var material_name = data[i]?.Material_Name;
    var quantity = data[i]?.Quantity;
    var material_data = {
      materialName: material_name,
      qty: quantity,
    };
    material_datas.push(material_data);

    var mat_po = {
      materialName: data[i]?.Mat_PO_ID?.Material_Name,
      qty: data[i]?.Mat_PO_ID?.Quantity,
    };
    mat_pos.push(mat_po);
  }

  var mat_PO = mat_pos.filter(
    (v, i, a) => a.findIndex((t) => t.materialName === v.materialName) === i
  );

  let material_content = [];
  for (var i = 0; i < mat_PO.length; i++) {
    let m_name = mat_PO[i]?.materialName;
    var d_ = material_datas.filter((p) => p.materialName == m_name);
    var mat_ = d_.map((p) => p.qty);
    material_content.push(mat_);
  }
  // console.log(material_content)
  var d = [];
  for (var i = 0; i < material_content.length; i++) {
    var m_c = material_content[i];
    var d_c = 0;
    for (var j = 0; j < m_c.length; j++) {
      d_c += Number(m_c[j]);
    }
    d.push(d_c);
  }

  var result = [];
  for (var i = 0; i < mat_PO.length; i++) {
    var content = mat_PO[i];
    var params = {
      total: d[i],
      mat_name: content?.materialName,
      qty: Number(content?.qty),
      pending: Number(content?.qty) - d[i],
    };
    result.push(params);
  }

  return result;
}

// CK Editor
var myeditor;
function ckEditor(id) {
  ClassicEditor.create(document.querySelector(`#${id}`))
    .then((editor) => {
      // console.log(editor);
      myeditor = editor;
    })
    .catch((error) => {
      // console.error(error);
    });
}
