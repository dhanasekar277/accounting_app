$(document).ready(function () {
 
    var base = window.location.protocol + "//" + window.location.host+'/';
    var url = base+'api/'
    var urls = 'asdsadsad'
    // console.log(url)
    var csrftoken = $('meta[name="csrf-token"]').attr('content')
    $('#example').DataTable()

    $.ajaxSetup({
        headers:
            { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') }
    });


    // Note the async keyword
    function GetData(dynamic_url){
        var data;
        $.ajax({
            url: dynamic_url,
            type: 'GET',
            async: false,
            success: function (response) {
                data = response
                // callback.call(data)
            },
            cache: false,
            contentType: false,
            processData: false
        });

        return data
    }

    // agency select
    $.get(url+'agency/', function (res){
        // agency result
        let result = res?.results

        // active agency
        var active_agency = result.filter(p => p.Active == true)
        // console.log(active_agency)
        $('#agencyid').attr('agency-id',active_agency[0]?.id)
        $('.heading .agency, table .agency_head').html(active_agency[0]?.Name)
        $('#SelectCompany').append('<option value="'+active_agency[0]?.id+'">'+active_agency[0]?.Name+'</option>')
        // agency append
        for(var i=0;i<result.length;i++){
            if(result[i]?.Active == false){
                $('#SelectCompany').append('<option value="'+result[i]?.id+'">'+result[i]?.Name+'</option>')
            }
        }

    })

    // get order list data model
    $('.viewmaterial').click(function () {
        var materialid = $(this).attr('data-attr')
        $.get(url + 'order-list/' + materialid, function (data) {
            $('#viewmaterial .modal-title').text(data?.ProductName)
            $('#viewmaterial #company_name #name').text(data?.Name)
            $('#viewmaterial #company_name #cname').text(data?.CompanyName)
            $('#viewmaterial #hsncode #hsn').text(data?.Hsn_code)
            $('#viewmaterial #price #op').text(data?.OfferPrice)
            $('#viewmaterial #price #q').text(data?.Quantity)
            $('#viewmaterial #price #p').text(data?.Price)
        })

    })

    // select company name
    $('#SelectCompany').change(function () {
        // store it in session
        var id = $(this).val()
        $.get(base + 'agency/' + id, function (res) {
            if (res.status == 200) {
                $('#agencyupdatestatus').text(res.message)
                setTimeout(() => {
                    location.reload()
                }, 1000)
            }
        })
    })

    // customer phone
    $('.customer_ph').click(function(e){
        var cu_id = $(this).attr('cu-id')
        let cdata = GetData(url+'customers/'+cu_id)

        $(`#customerPhoneNumber #Founder_Phone`).html('')
        let founder_phone = cdata?.Founder_Phone
        if(founder_phone.length != 0){
            founder_phone.forEach(ele => {
                $(`#customerPhoneNumber #Founder_Phone`).append(`<a class="ms-2" href="tel:${ele?.Phone_Number}">${ele?.Phone_Number}</a>`)
            })
        }else{
            $(`#customerPhoneNumber #Founder_Phone`).append(`No Numbers.`)
        }

        $(`#customerPhoneNumber #Customer_Staff_Account`).html('')
        let customer_staff_account = cdata?.Customer_Staff_Account
        if(customer_staff_account.length != 0){
            customer_staff_account.forEach(ele => {
                $(`#customerPhoneNumber #Customer_Staff_Account`).append(`<div><a class="text-capitalize" href="tel:${ele?.Contact_No}">${ele?.Name}</a> - ${ele?.Position}</div>`)
            })
        }else{
            $(`#customerPhoneNumber #Customer_Staff_Account`).append(`No Numbers.`)
        }

        $(`#customerPhoneNumber #Bank_Account`).html('')
        let bank_account = cdata?.Bank_Account
        if(bank_account.length != 0){
            bank_account.forEach(ele => {
                $(`#customerPhoneNumber #Bank_Account`).append(`<div><a href="tel:${ele?.Register_Phone}">${ele?.Account_Holder_Name}</a> - ${ele?.Branch}</div>`)
            })
        }else{
            $(`#customerPhoneNumber #Bank_Account`).append(`No Numbers.`)
        }

        $(`#customerPhoneNumber #GST_No`).html('')
        let gst_no = cdata?.GST_No
        if(gst_no.length != 0){
            gst_no.forEach(ele => {
                $(`#customerPhoneNumber #GST_No`).append(`<div><a href="tel:${ele?.Mobile}" class="text-capitalize">${ele?.Holder_Name}</a></div>`)
            })
        }else{
            $(`#customerPhoneNumber #GST_No`).append(`No Numbers.`)
        }

        $(`#customerPhoneNumber #delivery_address`).html('')
        let branch = cdata?.Branches
        // console.log(branch)
        if(branch.length != 0){
            for(var i=0;i<branch.length;i++){
                let ba = branch[i]?.Billing_Address
                $('#customerPhoneNumber #delivery_address').append(`<div><b>Billing Address :</b> <a href="tel:${ba?.Mobile}" class="text-capitalize" id="delivery_phone">${ba?.Holder_Name}</a></div>`)
                let sd = branch[i]?.Staff_Detail
                if(sd.length != 0){
                    $('#customerPhoneNumber #delivery_address').append(`<b>Staff :</b>`)
                    for(var j=0;j<sd.length;j++){
                        $('#customerPhoneNumber #delivery_address').append(`<a href="tel:${sd[j]?.Contact_No}" class="mx-1 text-capitalize" id="delivery_phone">${sd[j]?.Name}</a>`)
                    }
                }

            }
        }else{
            $(`#customerPhoneNumber #delivery_address`).html('No Numbers.')
        }


        $('#customerPhoneNumber').modal('toggle')
    })

    // select vendors
    $('#selectVendor').change(function () {
        var vendorid = $(this).val()
        $.get(url + 'vendors/' + vendorid, function (data) {
            $('#vendorname').val(data?.Name)
            $('#vendorid').val(data?.id)
            $('#vendormobile').val(data?.Mobile)
            $('#vendoremail').val(data?.Email)
        })
    })

    $('#customercompanyname').change(function () {
        var id = $(this).val()
        $.get(url + 'customers/' + id, function (data) {
            $('#customername').val(data?.CustomerName)
            $('#customerid').val(data?.id)
            $('#customermobile').val(data?.Mobile)
            $('#customeremail').val(data?.Email)
            $('#customeraddress').val(data?.Address)
            $('#customerstate').val(data?.State)
            $('#customercity').val(data?.City)
            $('#customerzip').val(data?.Zip)
            $('#customercountry').val(data?.Country)
        })
    })

    $('#PatchMethod').change(function () {
        var key = $(this).attr('data-col')
        var url = $(this).attr('data-url')
        var id = $(this).attr('data-id')
        var value = $(this).val()
        PATCHMethod(key, value, url + '/' + id + '/')
    })



    $('.productupdate .update').click(function () {
        var params = {
            "Product": $('#productName').val(),
            "Price": $('#productPrice').val(),
            "GST": $('#productGST').val()
        }
        producturl = $(this).attr('data-url')
        id = $(this).attr('data-id')
        var urls = url + producturl + '/' + id + '/'
        PATCHPARAMMethod(params, urls)
        location.reload()
    })

    function PATCHPARAMMethod(params, dynamicurl) {
        alert('works')
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


    // patch method
    function PATCHMethod(key, value, dynamicurl) {

        patch = { [key]: value };
        baseurl = url + dynamicurl
        $.ajax({
            type: 'PATCH',
            url: baseurl,
            data: JSON.stringify(patch),
            processData: false,
            contentType: "application/json",
            dataType: "json",
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function (response) {
                // console.log(response)
            },
            error: function (response) {
                // console.log(response);
            }
        });

    }



    $('#addproduct').click(function () {
        $.ajax({
            type: "POST",
            url: url + 'products/',
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                "Vendor": $('#vendor').val(),
                "Product": $('#productname').val(),
                "Price": $('#productprice').val(),
                "GST": $('#productgst').val(),
                "Agency": $('#agency').val(),
                "User": $('#user-id').attr('data-id')
            }),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function (response) {
                $('.alert').addClass('alert-success').removeClass('d-none alert-danger')
                $('.alert strong').text('Product added successfully. !!!')
                setTimeout(function () {
                    location.reload()
                }, 2000)
            },
            error: function (response) {

                $('.alert').removeClass('d-none').addClass('alert-danger')
                $('.alert strong').text('All Fields are required. !!!')
            }
        });
    })



    // var deleteProduct = document.getElementById('deleteMethod')
    // deleteProduct.addEventListener('show.bs.modal', function (event) {
    //     // Button that triggered the modal
    //     var button = event.relatedTarget
    //     // Extract info from data-bs-* attributes
    //     var id = button.getAttribute('data-bs-whatever')
    //     // If necessary, you could initiate an AJAX request here
    //     $('#deleteMethod .dlt').attr('data-id', id)
    //     DELETEMethod()
    // })
    function DELETEMethod() {
        $('#deleteMethod .dlt').click(function () {
            var customurl = $(this).attr('data-url')
            var key = $(this).attr('data-col')
            var value = $(this).attr('data-id')
            var baseurl = url + customurl + '/' + value
            var params = { [key]: value };
            $.ajax({
                type: "DELETE",
                url: baseurl,
                contentType: "application/json",
                dataType: "json",
                data: JSON.stringify(params),
                headers: {
                    'X-CSRFToken': csrftoken
                },
            });
            $('.row_' + value).remove()
            $('#deleteMethod').modal('toggle');
        })
    }



    // daily order info
    // Example starter JavaScript for disabling form submissions if there are invalid fields
    (function () {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.querySelectorAll('.daily-order-needs-validation')

        // Loop over them and prevent submission
        Array.prototype.slice.call(forms)
            .forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }

                    if (form.checkValidity()) {
                        event.preventDefault()
                        var params = {
                            User: Number($('#userid').val()),
                            Order_recived_date: $('#orderreciveddate').val(),
                            Delivery_date: $('#orderdeliverydate').val(),
                            Billing_company_name: Number($('#agencyid').val()),
                            Sales_company_name: Number($('#customercompanyname').val()),
                            Purchase_transport_name: Number($('#selectVendor').val()),
                            Unloading_address: $('#drivercontactname').val(),
                            Unloading_state: $('#customerstate').val(),
                            Unloading_city: $('#customercity').val(),
                            Unloading_zip: $('#customerzip').val(),
                            Unloading_country: $('#customercountry').val(),
                            Driver_contact_name: $('#drivercontactname').val(),
                            Driver_contact_number: $('#drivercontactnumber').val(),
                            Site_contact_name: $('#sitecontactname').val(),
                            Site_contact_number: $('#sitecontactnumber').val(),
                            PUR_rate: $('#purrate').val(),
                            PO_number: $('#ponumber').val(),
                            Sales_rate: 100,
                            CDC_number: $('#cdcnumber').val(),
                            IDC_number: $('#idcnumber').val(),
                            Materials: getorderList.split(','),
                            'csrfmiddlewaretoken': csrftoken
                        }

                        $.ajax({
                            type: "POST",
                            url: url + "daily-orders/",
                            contentType: "application/json",
                            dataType: "json",
                            data: JSON.stringify(params),
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                            success: function (response) {
                                localStorage.removeItem('order-items')
                                $('#message').html('<div class="alert alert-primary alert-dismissible fade show" role="alert"><strong>Daily Order Info</strong> Created successfully. !!!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                                setTimeout(function () {
                                    location.reload()
                                }, 3000)
                            },
                            error: function (response) {
                                // console.log(response);
                            }
                        });
                    }

                    form.classList.add('was-validated')
                }, false)
            })
    })();



    // order list functionalities
    // Example starter JavaScript for disabling form submissions if there are invalid fields
    (function () {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.querySelectorAll('.order-list')

        // Loop over them and prevent submission
        Array.prototype.slice.call(forms)
            .forEach(function (form) {

                form.addEventListener('submit', function (event) {

                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }

                    if (form.checkValidity()) {
                        event.preventDefault()
                        var formData = $(this).serialize();
                        $('#orderslist').removeClass('d-none')
                        $.post(url + 'order-list/', formData, function (data) {
                            // console.log(data)
                            $('#orderslist').append('<tr><td>' + data.ProductName + '</td><td>' + data.Name + '<br><small>(' + data.CompanyName + ')</small></td><td><div><b>Price :</b>' + data.Price + '</div><div><b>Offer Price :</b><span>' + data.OfferPrice + '</span></div></td><td><a href="' + data.id + '" class="editorderlist text-warning"><span data-feather="edit"></span></a><a href="' + data.id + '" class="deleteorderlist text-danger"><span data-feather="trash-2"></span></a></td></tr>')
                            $('.order-list').trigger("reset");
                            localstorageset('order-items', data.id)
                        })
                    }

                    form.classList.add('was-validated')

                }, false)
            })
    })();




    // Form Validation for Login, Logout and Forgot Password 
    (function () {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.querySelectorAll('.needs-validation')

        // Loop over them and prevent submission
        Array.prototype.slice.call(forms)
            .forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }

                    form.classList.add('was-validated')
                }, false)
            })
    })();


    // Form validation for add vendor disabling form submissions if there are invalid fields
    (function () {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.querySelectorAll('.addvendor')

        // Loop over them and prevent submission
        Array.prototype.slice.call(forms)
            .forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }

                    form.classList.add('was-validated')
                }, false)
            })
    })();

    // delete products from orders
    function localstorageset(data, id) {
        var getData = localStorage.getItem(data)
        if (getData == null) {
            localStorage.setItem(data, id)
            // console.log('new order item')
        } else {
            var orderitem = getData.split(',')
            orderitem.push(id)
            var orders = orderitem.toString()
            localStorage.setItem(data, orders)
            // console.log('update item')
        }
    }

    $('#FinalOrderSubmit').click(function () {
        var data = localStorage.getItem('order-items')
        if (data != null) {
            items = data.split(',')
            userid = $('#userid').val()

            var params = {
                'Order': items,
                'User': userid,
                'csrfmiddlewaretoken': csrftoken
            }
            // console.log(params)

            $.post(url + 'orders/', params, function (data) {
                // console.log(data)
                localStorage.removeItem('order-items')
                location.reload()
            })

        } else {
            alert('add atleast one product.')
        }
    })
    // quotation

    $('#quotionTable').on('click', '.quatotiondeleteMethod', function (event) {
        event.preventDefault()
        quotionId = $(this).attr('data-bs-whatever')
        $.ajax({
            type: 'DELETE',
            url: 'http://127.0.0.1:8000/api/daily-orders/' + quotionId + '/',
            data: { 'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content') },
            headers: { 'X-CSRFtoken': $('meta[name="csrf-token"]').attr('content') },
            success: function (data, status) {
                // console.log(data)
            }
        })

    })




})