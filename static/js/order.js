var csrftoken = $('meta[name="csrf-token"]').attr("content");
// po id
var PO_ID = getLocal("PO_ID");
// po products id
var P_ID = getLocal("P_ID");
// sales comapny
var SC = getLocal("SC");
// billing address
var BA = getLocal("BA");
// delivery address
var DA = getLocal("DA");
// po number id
var PO = getLocal("PO");

var PO_Table_Hidden_Check = PO_ID == null ? "d-none" : "";
var MAT_Hidden_Check = P_ID == null ? "d-none" : "";

let po_data_material = [];
let data_material = [];

if (PO_ID != null) {
  $(".po_table").addClass(PO_Table_Hidden_Check);
  for (var i = 0; i < PO_ID.length; i++) {
    var action_url = url + "po-material-info/" + PO_ID[i] + "/";

    var po_data = GetData(action_url);
    // console.log(po_data)
    po_data_material.push(po_data);

    // select material
    $(".SelectMaterial").append(
      `<option value="${po_data?.Material_Name}__${po_data?.id}__${po_data?.PO_Rate}__${po_data?.Moisture}__${po_data?.Moisture_No}__${po_data?.Quantity_Type}">${po_data?.Material_Name}</option>`
    );
    // po material id
    $("#pomaterialid").append(`
            <tr>
                <td>${po_data?.Material_Name}</td>
                <td>${po_data?.Quantity} ${po_data?.Quantity_Type}</td>
                <td>${po_data?.Load}</td>
                <td>${po_data?.PO_Rate}</td>
                <td><a href="${po_data?.id}" data-id="${po_data?.id}" data-url="po-material-info" class="deletePO"><i class="fa fa-trash"></i></a></td>
            </tr>
        `);
  }
}

if (P_ID == null) {
  $(".materialtable").addClass(MAT_Hidden_Check);
} else {
  for (var i = 0; i < P_ID.length; i++) {
    if (P_ID[i] != "") {
      var action_url = url + "material-info/" + P_ID[i];
      var mat = GetData(action_url);

      data_material.push(mat);
      var mosit =
        mat?.Moisture == 1
          ? 'Yes <span class="text-blue">( ' +
            mat?.Moisture_Number +
            " )</span>"
          : " No";
      var purchasePrice =
        mat?.Purchase_Price == null ? "" : mat?.Purchase_Price;

      $(".material_list").append(`
                <tr class="row_${mat?.id}">
                    <td>
                        <div>${mat?.Material_Name}</div>
                    </td>
                    <td>
                        <div class="text-primary">${mat?.Vendor?.Company_Name}</div>
                        <div class="text-capitalize"><i class="fa fa-map-marker"></i> : ${mat?.Location_Supply}</div>
                    </td>
                    <td>
                        <div>${mat?.Vendor_Type}<span class="text-blue">( ${mat?.Payment_Capability} )</span></div>
                        <div><i class="fa fa-truck"></i> : ${mat?.Load}</div>
                    </td>
                    <td>
                        <div class="mt-2" style="font-size: 16px;"> ${mat?.Quantity} </div>
                    </td>
                    <td>
                        <div><span>${mosit}</span></div>
                        <span class="text-primary text-capitalize">${mat?.Material_Term}</span>
                    </td>
                    <td>
                        <input type="text" value="${mat?.Current_Price}" class="form-control current${mat?.id}">
                    </td>
                    <td style="width: 12%;">
                        <input type="text" value="${purchasePrice}" class="form-control purchase${mat?.id}">
                    </td>
                    <td >
                        <input type="text" value="${mat?.Sale_Price}" class="form-control sale${mat?.id}">
                    </td>

                    
                    <td>
                        <a href="${mat?.id}" class="addPriceMaterial"><i class="fa fa-check fa-lg"></i></a>
                        <a href="${mat?.id}" data-url="material-info" class="deleteMaterials ms-3"><i class="fa fa-close fa-lg"></i></a>
                    </td>
                </tr>
            `);

      if (i === P_ID.length - 1) {
        CalculationPOANDMaterials(po_data_material, data_material);
      }
    }
  }
}

function CalculationPOANDMaterials(po, material) {
  var calculation_material = [];
  for (var i = 0; i < po.length; i++) {
    let material_list = material.filter((p) => p?.Mat_PO_ID?.id == po[i]?.id);
    // console.log(material_list);
    var quantity_ = 0;
    for (var j = 0; j < material_list.length; j++) {
      let quantity = Number(material_list[j]?.Quantity);
      quantity_ += quantity;
    }
    $(".remainingQty").append(`
            <tr>
                <td>${material_list[0]?.Material_Name}</td>
                <td>${material_list[0]?.Mat_PO_ID?.Quantity}</td>
                <td>${quantity_}</td>
                <td>${
                  Number(material_list[0]?.Mat_PO_ID?.Quantity) - quantity_
                }</td>
            </tr>
        `);
  }

  // $('.remainingQty').append()
}

function SetDeliveryLocal() {
  var x = document.getElementById("deliveryaddress").value;
  SetLocalString("DA", x);
}

function SetBillingLocal() {
  var x = document.getElementById("billingaddress").value;
  SetLocalString("BA", x);
}

document
  .getElementById("deliveryaddress")
  .addEventListener("change", SetDeliveryLocal);
document
  .getElementById("billingaddress")
  .addEventListener("change", SetBillingLocal);

// sales company check
if (SC != null) {
  $("#sales_company_name").val(SC);
}
// billing address check
if (BA != null) {
  $("#billingaddress").val(BA);
}
// delivery address check
if (DA != null) {
  $("#deliveryaddress").val(DA);
}
// po detail check
if (PO != null) {
  // console.log(PO)
  $(".afterpo").html("");
  var action_url = url + "po-number/" + PO + "/";
  var data = GetData(action_url);
  // console.log(data)
  var remark =
    data?.Remarks.length > 0
      ? "<span class='fw-bold'>Remarks </span> : " + data?.Remarks
      : "";

  if (data?.PO_Type == "NA") {
    $(".afterpo").html(`
            <div><span class="text-danger fw-bold">Status</span> : Not Applicable</div>
            <div>
                <span class="fw-bold">Recieved </span> : ${data?.Order_Recieved_Date} 
                <span class="fw-bold ms-2">Expected </span> : ${data?.Order_Expected_Date} 
            </div>
            <div>${remark}</div>
        `);
  } else {
    $(".afterpo").html(`
            <div><span class="text-danger fw-bold">Status</span> : Applicable ( ${data?.PO_Number} )</div>
            <div>
                <b>Reciever</b> : <a  href="mailto:${data?.PO_Reciver_Mail}" class="text-capitalize">${data?.PO_Reciver_Name}</a>
                <b class="ms-2">Approved By</b> : <span class="text-capitalize">${data?.PO_Approved_By}</span>
            </div>
            <div>
                <span class="fw-bold">Recieved </span> : ${data?.Order_Recieved_Date} 
                <span class="fw-bold ms-2">Expected </span> : ${data?.Order_Expected_Date} 
            </div>
            <div>${remark}</div>
        `);
  }
}

// sales comapny on change get data
$("#sales_company_name").change(function (e) {
  var sales_company = $(this).val();
  localStorage.setItem("SC", sales_company);
  let s_comp = sales_company.replace("&", "%26");
  var action_url = url + "customers/?Company_Name=" + s_comp;
  var _data = GetData(action_url);
  // console.log(_data);
  // check gst user or not
  if (_data.results[0]?.GST_Type == "0") {
    // registered User

    // check there is gst no (billing address)
    var GST_No = _data.results[0]?.GST_No;
    var Branches = _data.results[0]?.Branches;

    $(".deliveryList .billingaddress, .deliveryList .deliveryaddress").html("");
    $(
      ".deliveryList, .deliveryList .billingaddress, .deliveryList .ba, .deliveryList .da"
    ).removeClass("d-none");

    if (GST_No.length != 0) {
      for (var i = 0; i < GST_No.length; i++) {
        if (GST_No[i]?.Address != null) {
          $(".deliveryList .billingaddress").append(`
              <div class="text-capitalize text-dark">(GST) ${GST_No[i]?.Address}, ${GST_No[i]?.City} - ${GST_No[i]?.Zip}, ${GST_No[i]?.State}, ${GST_No[i]?.Country}
                  <a href="${GST_No[i]?.id}" data-address="${GST_No[i]?.Address}" data-city="${GST_No[i]?.City}" data-zip="${GST_No[i]?.Zip}" data-state="${GST_No[i]?.State}" data-country="${GST_No[i]?.Country}" class="float-end selectBillingAddress text-success" ><i class="fa fa-check"></i></a>
              </div>
          `);
        }
      }
    }

    if (Branches.length != 0) {
      for (var i = 0; i < Branches.length; i++) {
        // console.log(Branches[i]?.Billing_Address?.Address);
        if (Branches[i]?.Billing_Address?.Address != null) {
          $(".deliveryList .billingaddress").append(`
              <div class="text-capitalize text-dark">(Branch) ${Branches[i]?.Billing_Address?.Address}, ${Branches[i]?.Billing_Address?.City} - ${Branches[i]?.Billing_Address?.Zip}, ${Branches[i]?.Billing_Address?.State}, ${Branches[i]?.Billing_Address?.Country}
              <a href="${Branches[i]?.id}" data-address="${Branches[i]?.Billing_Address?.Address}" data-city="${Branches[i]?.Billing_Address?.City}" data-zip="${Branches[i]?.Billing_Address?.Zip}" data-state="${Branches[i]?.Billing_Address?.State}" data-country="${Branches[i]?.Billing_Address?.Country}" class="float-end selectBillingAddress text-success" ><i class="fa fa-check"></i></a>
              </div>
          `);
        }

        var deliveryAddress = Branches[i]?.Delivery_Address;

        for (var j = 0; j < deliveryAddress.length; j++) {
          if (deliveryAddress[j]?.Address != null) {
            $(".deliveryList .deliveryaddress").append(`
              <div class="text-capitalize text-dark">(${deliveryAddress[j]?.NickName}) ${deliveryAddress[j]?.Address}, ${deliveryAddress[j]?.City} - ${deliveryAddress[j]?.Zip}, ${deliveryAddress[j]?.State}, ${deliveryAddress[j]?.Country}
                  <a href="${deliveryAddress[j]?.id}" data-address="${deliveryAddress[j]?.Address}" data-city="${deliveryAddress[j]?.City}" data-zip="${deliveryAddress[j]?.Zip}" data-state="${deliveryAddress[j]?.State}" data-country="${deliveryAddress[j]?.Country}" class="float-end selectDeliveryAddress text-success" ><i class="fa fa-check"></i></a>
              </div>
            `);
          }
        }
      }
    } else {
      $(".deliveryList .da").addClass("d-none");
    }
    let customerDeleveriAddress = _data.results[0];
    if (customerDeleveriAddress.delivery_Address) {
      $(".deliveryList .deliveryaddress").append(`
      <div class="text-capitalize text-dark">(Main) ${customerDeleveriAddress.delivery_Address}, ${customerDeleveriAddress.delivery_City} - ${customerDeleveriAddress.delivery_Zip}, ${customerDeleveriAddress.delivery_State}, ${customerDeleveriAddress.delivery_Country}
        <a href="${customerDeleveriAddress.id}" data-address="${customerDeleveriAddress.delivery_Address}" data-city="${customerDeleveriAddress.delivery_City}" data-zip="${customerDeleveriAddress.delivery_Zip}" data-state="${customerDeleveriAddress.delivery_State}" data-country="${customerDeleveriAddress.delivery_Country}" class="float-end selectDeliveryAddress text-success" ><i class="fa fa-check"></i></a>
      </div>
    `);
    }
  } else {
    alert("Un Registered User. !!!");
  }


  // select Billing Address
  selectAddress();
});

// select delivery address and billing address
function selectAddress() {
  // select billing address
  $(".selectBillingAddress").click(function (e) {
    e.preventDefault();
    var data_address = $(this).attr("data-address");
    var data_city = $(this).attr("data-city");
    var data_zip = $(this).attr("data-zip");
    var data_state = $(this).attr("data-state");
    var data_country = $(this).attr("data-country");
    var billing = `${data_address}, ${data_city} - ${data_zip}, ${data_state}, ${data_country}`;
    $("#billingaddress").val(billing);
    $(".deliveryList .billingaddress, .deliveryList .ba").addClass("d-none");
    SetLocalString("BA", billing);
  });

  // select delivery address
  $(".selectDeliveryAddress").click(function (e) {
    e.preventDefault();
    var data_address = $(this).attr("data-address");
    var data_city = $(this).attr("data-city");
    var data_zip = $(this).attr("data-zip");
    var data_state = $(this).attr("data-state");
    var data_country = $(this).attr("data-country");
    var delivery = `${data_address}, ${data_city} - ${data_zip}, ${data_state}, ${data_country}`;
    $("#deliveryaddress").val(delivery);
    $(".deliveryList .deliveryaddress, .deliveryList .da").addClass("d-none");
    SetLocalString("DA", delivery);
  });
}

//  select po type
$("#Order_PO_Type").change(function (e) {
  e.preventDefault();
  var po_type = $(this).val();
  if (po_type == "PA") {
    $(".podetail").html(`
            <form id="add_po_number">
            <div class="row">
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
            <div class="col-12">
                <label for="PO_Number" class="form-label small fw-bold mb-1">PO Number</label>
                <input type="hidden" class="form-control form-control-sm" id="PO_Type" value="${po_type}" name="PO_Type">
                <input required type="text" class="form-control form-control-sm" id="PO_Number"  name="PO_Number">
            </div>
            <div class="col-12">
                <label for="Scan_Copy" class="form-label small fw-bold mb-1">Scan Copy</label>
                <input type="file" class="form-control form-control-sm" id="Scan_Copy" name="Scan_Copy">
            </div>
            <div class="col-6 mt-1 pe-1">
                <label for="PO_Recived_From_Name" class="form-label small fw-bold mb-1">PO Reciver Name</label>
                <input required type="text" class="form-control form-control-sm" id="PO_Recived_From_Name" name="PO_Reciver_Name">
            </div>
            <div class="col-6 mt-1 ps-1">
                <label for="PO_Recived_From_Mail" class="form-label small fw-bold mb-1">PO Reciver Mail</label>
                <input required type="text" class="form-control form-control-sm" id="PO_Recived_From_Mail" name="PO_Reciver_Mail">
            </div>
            <div class="col-6 pe-1 mt-1">
                <label for="PO_Approved_By" class="form-label small fw-bold mb-1">PO Approved By</label>
                <input required type="text" class="form-control form-control-sm" id="PO_Approved_By"
                    name="PO_Approved_By">
            </div>
            <div class="col-6 ps-1 mt-1">
                <label for="PO_Date" class="form-label small fw-bold mb-1">PO Date</label>
                <input required type="date" class="form-control form-control-sm" id="PO_Date" name="PO_Date">
            </div>
            <div class="col-6 mt-1 pe-1">
                <label for="Order_Recieved_Date" class="form-label small fw-bold mb-1">Order Recieved Date</label>
                <input required type="date" class="form-control form-control-sm" id="Order_Recieved_Date" name="Order_Recieved_Date">
            </div>
            <div class="col-6 mt-1 ps-1">
                <label for="deliverydate" class="form-label small fw-bold mb-1">Expected Delivery Date</label>
                <input required type="date" class="form-control form-control-sm" id="deliverydate" name="Order_Expected_Date">
            </div>
            <div class="mt-1">
                <label for="Remarks" class="form-label small fw-bold mb-1">Remarks :</label>
                <textarea name="Remarks" id="Remarks" value="none" class="form-control form-control-sm" rows="2"></textarea>
            </div>
            <div class="col-12 mt-1">
                <button type="submit" class="btn btn-sm btn-primary w-100 py-0 mt-2 small " id="addPO"><i class="fa fa-plus"></i> Add PO</button>
            </div>
            </div>
            </form>
        `);
  } else {
    $(".podetail").html(`
            <form id="add_po_number">
            <div class="row">
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
            <div class="col-6 mt-1 pe-1">
                <label for="Order_Recieved_Date" class="form-label small fw-bold mb-1">Order Recieved Date</label>
                <input type="hidden" class="form-control form-control-sm" id="PO_Type" value="${po_type}" name="PO_Type">
                <input required type="date" class="form-control form-control-sm" id="Order_Recieved_Date"
                    name="Order_Recieved_Date">
            </div>
            <div class="col-6 mt-1 ps-1">
                <label for="deliverydate" class="form-label small fw-bold mb-1">Expected Delivery Date</label>
                <input required type="date" class="form-control form-control-sm" id="deliverydate" name="Order_Expected_Date">
            </div>
            <div class="mt-1">
                <label for="Remarks" class="form-label small fw-bold mb-1">Remarks :</label>
                <textarea name="Remarks" id="Remarks" class="form-control form-control-sm" rows="2"></textarea>
            </div>
            <div class="col-12 mt-1">
                <button type="submit" class="btn btn-sm btn-primary w-100 py-0 mt-2 small " id="addPO"><i class="fa fa-plus"></i> Add PO</button>
            </div>
            </div>
            </form>
        `);
  }

  Add_PO_Number();
});

// add po number
function Add_PO_Number() {
  $("#add_po_number").submit(function (e) {
    e.preventDefault();
    var data = new FormData(this);
    let action_url = url + "po-number/";
    var id = FormDataSubmit(action_url, data);
    localStorage.setItem("PO", id);
    alert("PO Details Added Successfully. !!!");
    location.reload();
  });
}

// select po material
$(".add_po_material").click(function (e) {
  e.preventDefault();
  // get po data
  var params = {
    Material_Name: $(".SelectPOMaterial").val(),
    Quantity: $("#po_quantity").val(),
    Quantity_Type: $("#quantity_type").val(),
    Load: $("#po_load").val(),
    PO_Rate: $("#po_rates").val(),
    Moisture: $("#moisture").val(),
    Moisture_No: $("#moisture_number").val(),
    PO_Terms: $("#po_terms").val(),
    csrfmiddlewaretoken: csrftoken,
  };

  var action_url = url + "po-material-info/";
  PostData(action_url, params, "PO_ID");
  $(".poalert").removeClass("d-none");
  setTimeout(() => {
    location.reload();
  }, 400);

  // var Quantity = $('#po_quantity').val()
  // var Quantity_Type = $('#quantity_type').val()
  // var PO_Rate = $('#po_rates').val()
  // var FinalPrice = PriceCalculation(Quantity, Quantity_Type, PO_Rate)
  // console.log(FinalPrice)
});

// select po materials
$(".SelectMaterial").change(function (e) {
  e.preventDefault();
  var _material = $(this).val();
  var material = _material.split("__");
  var material_name = material[0];
  var po_material_id = material[1];
  var po_rate = material[2];
  var moisture = material[3] == 1 ? "Yes" : "No";
  var moisture_no = material[4];
  var quantity_type = material[5];

  var action_url = url + "products/?Product=" + material_name;
  var data = GetData(action_url);

  // check material count
  var _data = data?.results.sort(function (a, b) {
    return a?.AvgPrice - b?.AvgPrice;
  });
  // console.log(_data);
  if (data?.results.length != 0) {
    $(".priceTable").removeClass("d-none");
    for (var i = 0; i < _data.length; i++) {
      var d = _data[i];
      // console.log(d);
      var Qua = _data[i]?.Quality;
      var mf = _data[i]?.Material_Supplying[0]?.Material_From;
      var mt = _data[i]?.Material_Supplying[0]?.Material_To;
      var lp = _data[i]?.LatestPrice;
      // console.log(mt);

      let mt_ = mt.map((p) => p.District);

      let meterialtostr = JSON.stringify(mt_);

      $("#pricelist").append(`
                <tr>
                    <td>
                        <div>${d?.Vendor?.Vendor_Name}</div>
                        <div class='small text-primary'>( ${d?.Vendor?.Company_Name} )</div>
                        <div><small>Type</small> : ${d?.Vendor?.Vendor_Type}</div>
                        <b class="text-success">Origin :</b>
                        <ul class='org${d?.id} text-capitalize ps-3 mb-0'></ul>
                        <b class="text-success">Material To :</b>
                        <ul class='m_t${d?.id} text-capitalize ps-3 mb-0'></ul>
                    </td>
                    <td>
                        <ul id="qu${d?.id}" class="ps-3 mb-0"></ul>
                        <div><b class='text-primary'>GST : </b>${d?.GST}</div>
                    </td>
                    <td>${d?.Vendor?.Payment_Capabilities}</td>
                    <td style="width:22%" class="selectLatestPrice${d?.id}">
                        <select class="lp${d?.id} form-control LatestPrice form-control-sm">

                        </select>
                        <button id="${d?.id}" class="btn btn-sm btn-primary px-1 py-0 mt-1 new_price"><i class="fa small fa-12 fa-plus"></i> New Price</button>
                    </td>
                    <td style="width:22%" class="addLatestPrice${d?.id}">
                        
                    </td>
                    <td>
                        <a  data-name='${d?.Vendor?.Vendor_Name}' 
                            data-id='${d?.Vendor?.id}' 
                            data-company='${d?.Vendor?.Company_Name}' 
                            mat_po_id='${po_material_id}' 
                            data-produtid='${d?.id}' 
                            data-gst='${d?.GST}' 
                            data-po-rate='${po_rate}'
                            data-hsnc='${d?.HSNCode}'
                            data-moisture = '${moisture}'
                            moisture = '${material[3]}'
                            data-moisture-no = '${moisture_no}'
                            data-capabilties='${d.Vendor?.Payment_Capabilities}' 
                            data-qt = '${quantity_type}'
                            data-mat-to = '${meterialtostr}'
                            data-vendor-type='${d.Vendor?.Vendor_Type}' class='btn btn-primary btn-sm SelectProduct py-0'><i class="fa fa-plus"></i></a>
                    </td>
                </tr>
            `);

      // quality price
      for (var j = 0; j < Qua.length; j++) {
        $("#qu" + d?.id).append(
          `<li>${Qua[j]?.Quality} <span class="text-success fw-bold">${Qua[j]?.Price}</span></li>`
        );
      }

      for (var j = 0; j < mt.length; j++) {
        $(".m_t" + d?.id).append(`<li>${mt[j]?.District}</li>`);
      }

      // orgin of the material -  material from
      for (var j = 0; j < mf.length; j++) {
        $(".org" + d?.id).append(`<li>${mf[j]?.Location}</li>`);
      }

      var latest = lp.sort(function (a, b) {
        return new Date(b.date) - new Date(a.date);
      });

      if (latest.length == 0) {
        $(".addLatestPrice" + d?.id).html(`
                    <input type="text" class="form-control LatestPrice form-control-sm" placeholder="Latest Price" >
                `);
        $(".selectLatestPrice" + d?.id).addClass("d-none");
      } else {
        for (var j = 0; j < latest.length; j++) {
          $(".lp" + d?.id).append(`<option 
                        value="${latest[j]?.Price}">
                        ${latest[j]?.Price}  &nbsp; / &nbsp; ${latest[j]?.date}
                    </option>`);
        }
        $(".addLatestPrice" + d?.id).addClass("d-none");
      }
    }

    SelectProduct();
    // add new price
    AddNewPrice();
  }
});

// delete po materials
$(".deleteMaterials").click(function (e) {
  e.preventDefault();
  var _id = $(this).attr("href");
  var dataurl = $(this).attr("data-url");
  var _url = url + dataurl + "/" + _id + "/";
  // console.log(action_url);
  DeleteData(_id, _url);
  removeLocal(_id, "P_ID");
});

function SelectProduct() {
  $(".SelectProduct").click(function (e) {
    let material_name = $(this).val();
    let vendor_name = $(this).attr("data-name");
    let vendor_id = $(this).attr("data-id");
    let vendor_company = $(this).attr("data-company");
    let material_to = $(this).attr("data-mat-to");
    let po_id = $(this).attr("mat_po_id");
    let product_id = $(this).attr("data-produtid");
    let gst = $(this).attr("data-gst");
    let po_rate = $(this).attr("data-po-rate");
    let hsnc = $(this).attr("data-hsnc");
    let capabilties = $(this).attr("data-capabilties");
    let vendor_type = $(this).attr("data-vendor-type");
    let moisture = $(this).attr("data-moisture");
    let moisture_no = $(this).attr("data-moisture-no");
    let moist = $(this).attr("moisture");
    let qtype = $(this).attr("data-qt");
    // console.log(qtype);

    var hsn_code = hsnc == null ? "" : hsnc;
    var selector = ".addLatestPrice" + product_id + " .LatestPrice";

    var price = $(selector).val();

    if (price == "" || price == undefined) {
      var selector = ".selectLatestPrice" + product_id + " .LatestPrice";
      var price = $(selector).val();
    }

    const product_url = url + "products/" + product_id + "/";
    var get_data = GetData(product_url);
    var lp = get_data?.LatestPrice;
    var prices = [];
    for (var i = 0; i < lp.length; i++) {
      prices.push(lp[i].Price);
    }

    if (prices.includes(price) == false) {
      var action_url = url + "latest-price/";
      var params = {
        Price: price,
        csrfmiddlewaretoken: csrftoken,
      };
      PostData(action_url, params, "T");

      setTimeout(function () {
        var price_id = localStorage.getItem("T");

        var get_url = base + "post-api/products/" + product_id + "/";
        var getlp = GetData(get_url);

        var lp = getlp?.LatestPrice;
        lp.push(price_id);

        var params = {
          LatestPrice: lp,
        };

        localStorage.removeItem("T");

        $.ajax({
          type: "PATCH",
          url: get_url,
          data: JSON.stringify(params),
          processData: false,
          contentType: "application/json",
          dataType: "json",
          headers: {
            "X-CSRFToken": csrftoken,
          },
          success: function (response) {
            alert("New Price Added. !!!");
          },
          error: function (response) {
            alert("Network issue Try again later. !!!");
          },
        });
      }, 400);
    }
    // console.log(material_to);
    let mat_to = JSON.parse(material_to);
    console.log(mat_to)
    for (var i = 0; i < mat_to.length; i++) {
      $(".materialDetail #location_supplysel").append(
        `<option value="${mat_to[i]}">${mat_to[i]}</option>`
      );
    }

    e.preventDefault();
    $(".materialDetail #v_name").val(vendor_name);
    $(".materialDetail #v_company").val(vendor_company);
    $(".materialDetail #v_type").val(vendor_type);
    $(".materialDetail #v_payment").val(capabilties);
    $(".materialDetail #Material_Name").val(material_name);
    $(".materialDetail #Price").val(po_rate);
    $(".materialDetail #Vendor_Id").val(vendor_id);
    $(".materialDetail #Mat_PO_id").val(po_id);
    $(".materialDetail #Product_id").val(product_id);
    $(".materialDetail #Purchase_Price").val(price);
    $(".materialDetail #HSNCode").val(hsn_code);
    $(".materialDetail #Moisture").val(moisture);
    $(".materialDetail #moisture_id").val(moist);
    $(".materialDetail #Moisture_Number").val(moisture_no);
    $(".materialDetail #quantityType").val(qtype);
    $(".priceTable table").addClass("d-none");
    $("#pricelist").html("");
  });
}

// moisture select
$("#moisture").change(function (e) {
  var moisture = $(this).val();
  // console.log(moisture);
  if (moisture == 0) {
    $("#moisture_number").attr("disabled", true);
  } else {
    $("#moisture_number").attr("disabled", false);
  }
});

$(".deletePO").click(function (e) {
  e.preventDefault();
  var _id = $(this).attr("data-id");
  var _url = $(this).attr("data-url");
  var _url = url + _url + "/" + _id + "/";
  // console.log(_url);
  DeleteData(_id, _url);
  removeLocal(_id, "PO_ID");
});

// add material
$("#add_materials").click(function (e) {
  var material = $(".SelectMaterial").val();
  var mat_name = material.split("__")[0];

  var params = {
    Product_Name: $("#Product_id").val(),
    Material_Name: mat_name,
    Vendor: $("#Vendor_Id").val(),
    Vendor_Type: $("#v_type").val(),
    Payment_Capability: $("#v_payment").val(),
    Quantity: $("#Quantity").val(),
    Quantity_Type: $("#quantityType").val(),
    Load: $("#No_Of_Load").val(),
    Current_Price: $("#Price").val(),
    Sale_Price: $("#Sales_Price").val(),
    Purchase_Price: $("#Purchase_Price").val(),
    Moisture: $("#moisture_id").val(),
    Moisture_Number: $("#Moisture_Number").val(),
    HSNCode: $(".materialDetail #HSNCode").val(),
    Others: $("#Others").val(),
    Material_Term: $("#Material_Term").val(),
    Location_Supply: $("#location_supply").val(),
    Mat_PO_ID: $("#Mat_PO_id").val(),
    User: $("#userid").text(),
    Expected_Date: $("#Expected_Date").val(),
    csrfmiddlewaretoken: csrftoken,
  };
  // console.log(params);
  var _url = base + "post-api/material-info/";
  PostData(_url, params, "P_ID");
  $(".material_messages").removeClass("d-none");
  setTimeout(() => {
    location.reload();
  }, 400);
});

// edit po materials
$(".addPriceMaterial").click(function (e) {
  e.preventDefault();
  var id = $(this).attr("href");
  // console.log(id);
  var currentSelector = ".current" + id;
  var saleSelector = ".sale" + id;
  var purchaseSelector = ".purchase" + id;

  var params = {
    Purchase_Price: $(purchaseSelector).val(),
    Sale_Price: $(saleSelector).val(),
    Current_Price: $(currentSelector).val(),
  };

  const action_url = url + "material-info/" + id + "/";

  // console.log(params);
  // console.log(action_url);

  PatchData(params, action_url);
});

// add final order submit functionality
$(".addOrder").click(function () {
  // check user status if admin
  if ($("#permission").attr("admin") == "False") {
    user_permission = false;
  } else {
    user_permission = true;
  }
  const material = P_ID.filter((p) => p.length);

  var sc = SC[0].replace("&", "%26");
  var action_url = url + "customers/?Company_Name=" + sc;
  var _data = GetData(action_url);
  var sales_company_id = _data?.results[0]?.id;

  var po_action_url = url + "po-number/" + PO[0] + "/";
  var mat_po_params = {
    PO_Material_Info: PO_ID,
  };

  PatchData1(mat_po_params, po_action_url);

  var params = {
    Sales_Delivery_Address: $("#deliveryaddress").val(),
    Billing_Address: $("#billingaddress").val(),
    Approved: user_permission,
    // Approved: 'False',
    User: $("#userid").text(),
    Agency: $("#SelectCompany").val(),
    Sales_Company: sales_company_id,
    PO_Number: PO[0],
    Materials: material,
    csrfmiddlewaretoken: csrftoken,
  };
  // console.log(params);

  // console.log(params);
  var action_url = base + "post-api/orders/";
  $.ajax({
    type: "POST",
    url: action_url,
    contentType: "application/json",
    dataType: "json",
    data: JSON.stringify(params),
    headers: {
      "X-CSRFToken": csrftoken,
    },
    success: function (response) {
      localStorage.removeItem("PO");
      localStorage.removeItem("DA");
      localStorage.removeItem("BA");
      localStorage.removeItem("P_ID");
      localStorage.removeItem("SC");
      localStorage.removeItem("PO_ID");
      alert("Material Added Successfully. !!!");
      PushNotification("Add", "orders", response.id);
      location.reload();
    },

    error: function (response) {
      alert("Network Error. !!!");
    },
  });
});

// add new price function
function AddNewPrice() {
  $(".new_price").click(function () {
    const id = $(this).attr("id");
    $(".lp" + id).remove();
    $(".selectLatestPrice" + id).html(`
            <input type="text" class="form-control LatestPrice form-control-sm" placeholder="Latest Price">
        `);
    $(".selectLatestPrice" + id)
      .attr("class", "")
      .addClass(`addLatestPrice${id}`);
  });
}

// Note the async keyword
function GetData(dynamic_url) {
  var data;
  $.ajax({
    url: dynamic_url,
    type: "GET",
    async: false,
    success: function (response) {
      data = response;
      // callback.call(data)
    },
    cache: false,
    contentType: false,
    processData: false,
  });

  return data;
}

// post data
function PostData(url, params, set) {
  $.post(url, params, function (res) {
    if (set != "") {
      // console.log(set, res?.id);
      setLocal(set, res?.id);
    }
  });
}

function FormDataSubmit(action_url, Formdata) {
  var data;
  $.ajax({
    url: action_url,
    type: "POST",
    data: Formdata,
    async: false,
    success: function (response) {
      data = response?.id;
      callback.call(data);
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

// delete data
function DeleteData(id, action_url) {
  var name = $("#user_name").attr("data-name");
  let person = prompt("Please Enter Your Name ?", "");

  if (person == name) {
    $.ajax({
      type: "DELETE",
      url: action_url,
      contentType: "application/json",
      dataType: "json",
      data: JSON.stringify({ id: id }),
      headers: {
        "X-CSRFToken": csrftoken,
      },
    });
    alert("Deleted Successfully. !!!");
    location.reload();
  } else {
    alert("Invalid Username");
  }
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

//
function PatchData(params, dynamicurl) {
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
    success: function (response) {
      alert("Material Updated. !!!");
      location.reload();
    },
    error: function (response) {
      alert("Network issue Try again later. !!!");
    },
  });
}

function PatchData1(params, dynamicurl) {
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

// price calculation
function PriceCalculation(qty, type, rate) {
  var pricecalc = Number(rate) * QuantityFormula(type, qty);
  return pricecalc;
}

// localstorage id store
function setLocal(data, id) {
  var getData = localStorage.getItem(data);
  if (getData == null) {
    localStorage.setItem(data, id);
  } else {
    var item = getData.split(",");
    item.push(id);
    var orders = item.toString();
    localStorage.setItem(data, orders);
  }
}

// get local storage data
function getLocal(data) {
  var local_data = localStorage.getItem(data);
  if (local_data == null) {
    return null;
  } else if (local_data == "") {
    return null;
  } else {
    var json = local_data.split(",");
    return json;
  }
}

// remove local
function removeLocal(id, data) {
  var getData = localStorage.getItem(data);
  let json_data = getData.split(",");
  // if(json_data)
  let index = json_data.indexOf(id);
  if (index > -1) {
    json_data.splice(index, 1);
  }
  var removed_data = json_data.toString();
  localStorage.setItem(data, removed_data);
}

function SetLocalString(key, value) {
  localStorage.setItem(key, value);
}

function PushNotification(type, model, id) {
  var notification = JSON.stringify({
    id: id,
    model: model,
  });
  var params = {
    User: $("#userid").html(),
    Types: type,
    Notifications: notification,
    csrfmiddlewaretoken: csrftoken,
    Status: Boolean($("#permission").attr("admin")),
  };
  // console.log(params)
  $.post(base + "post-api/notifications/", params, function (res) {
    // console.log(res)
  });
}
