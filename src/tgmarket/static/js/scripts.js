$(document).ready(function () {
    var form = $('#buying_form');
    console.log(form);

    function basketUpdating(product_id, is_delete) {
        var data = {};
        data.product_id = product_id;
        var csrf_token = $('#buying_form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data)
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.total_nmb);
                if (data.total_nmb || data.total_nmb == 0) {
                        $('#basket_total_nmb').text("(" + data.total_nmb + ")");
                        console.log(data.products);
                        $('.basket-items ul').html("");
                        $.each(data.products, function (k, v) {
                            $('.basket-items ul').append('<li>' + v.name + ',' + v.price + ' ' +
                                'Byn ' + '&nbsp;&nbsp;&nbsp;&nbsp;' + '&nbsp;&nbsp;&nbsp;&nbsp;' +
                                '<a class="delete-item" href="" data-product_id="' + v.id + '">x</a>' + '</li>');
                        })
                }
            },
            error: function () {
                console.log("error")
            }
        })

    }

    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var submint_button = $('#submit_button');
        var product_id = submint_button.data("product_id");
        var product_name = submint_button.data("product_name");
        var product_price = submint_button.data("product_price");
        console.log(product_id, product_name, product_price);
        basketUpdating(product_id, is_delete = false);
        $('.basket-items ul').append('<li>' + product_name + ',' + product_price + ' ' +
            'Byn ' + '&nbsp;&nbsp;&nbsp;&nbsp;' + '&nbsp;&nbsp;&nbsp;&nbsp;' +
            '' + '<a class="delete-item" href="">  x</a>' + '</li>');
    })

    function showingBasket() {
        $('.basket-items').toggleClass('d-none');
    };

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').mouseover(function () {
        showingBasket();
    });

    $('.basket-container').mouseout(function () {
        showingBasket();
    });

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
        product_id = $(this).data('product_id')
        basketUpdating(product_id, is_delete = true)
    })


});