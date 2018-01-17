$(document).ready(function () {
    //{#Форма, откуда выхватываем данные#}
    var form = $('.form_buy_product');

    //{#Описываем функцию для добавления, обновленрия или удаления товара#}

    function basketUpdating(filter_id, filter_article, filter_name, filter_brand, filter_price, numb, is_delete) {
        //  {#Создаем словарь, данные из которого пойдут в пост запрос  контроллер#}
        var data = {};
        data.filter_id = filter_id;
        data.filter_article = filter_article;
        data.filter_name = filter_name;
        data.filter_brand = filter_brand;
        data.filter_price = filter_price;
        data.numb = numb;
        //{#Если True, то товар нужно удалить, это значение мы отсылаем в контроллер#}
        if (is_delete) {
            data.is_delete = "1";
        } else {
            data.is_delete = "";
        }

        data["csrfmiddlewaretoken"] = $('#csrf').children()[0].value;
        var url = $('#csrf').attr("action");

        //{#console.log(data);#}
        $.ajax({
            //  {#КОнтроллер, куда мы посылаем данные для обработки#}
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                //     {#console.log("OK");#}
                //   {#console.log(data.filters_total_numb);#}
                $("#basket-total-numb").text("(" + data.filters_total_numb + ")");
                $(".basket-items ul").html("");
                //v-элемент списка(словарь)
                // {#products попадает из контроллера basket_adding это список словарей, в котором мы проходим по каждому словарю#}
                $.each(data.products, function (k, v) {
                    $(".basket-items ul").append('<li><a style="text-decoration: none ;" href="/filters/filter_card/' + v.id + '" title="filter_article filter_name filter_brand">' + v.article + " " + v.name + " " + v.numb + " шт. x " + v.price_per_item + " <i class=\"fa fa-rub\"></i> " + " = " + v.total_price + ' <i class="fa fa-rub"></i> <a  style="text-decoration: none ;"  class="delete-item" href="" data-filter_id="' + v.id + '"> <i class="fa fa-times" aria-hidden="true"></i></a></a></li>');
                });
                $(".basket-items ul").append('<li>Итого: ' + data.total_price_all_product + ' <i class="fa fa-rub"></i></li>');
                $("#cart_body").html("");
                $.each(data.products, function (k, v) {
                    $("#cart_body").append('<tr> <td><p>' + v.article + ' ' + v.name + '</p>' + '<input type="hidden" value="' + v.id + '" class="hidden"></td><td><span class="product_price">' + v.price_per_item + '</span></td><td><input class="w-50 product_amount" type="number" value="' + v.numb + '" min="1" step="1" name="product_in_bascket_"></td><td><span class="total_product_in_basket_amount">' + v.total_price + '</span></td><td><input type="checkbox" name="is_del" class="checkbox"></td></tr>')
                });
                calculatingBasketAmount();
            },
            error: function () {
                console.log("error")
            }
        });
    }

    //{#Полуаем данные, пришедшие на кнопку#}
    form.on("submit", function (e) {
        e.preventDefault();
        var numb = $("#number").val();
        if (numb === undefined) {
            numb = 1
        }
        //   console.log(numb);
        var submit_btn = $(this.sub);
        var filter_id = submit_btn.data("filter-id");
        var filter_article = submit_btn.data("article");
        var filter_name = submit_btn.data("name");
        var filter_brand = submit_btn.data("brand");
        var filter_price = submit_btn.data("price");
        var filter_category = submit_btn.data("category");
        // {#var total_price=submit_btn.data("total-price");#}

        basketUpdating(filter_id, filter_article, filter_name, filter_brand, filter_price, numb, is_delete = false)
    });

    $(".basket-container").mouseover(function () {
        $(".basket-items").removeClass("d-none");
    });

    $(".basket-container").mouseout(function () {
        $(".basket-items").addClass("d-none");
    });

    function calculatingBasketAmount() {
        var totalOrderAmount = 0;
        $(".total_product_in_basket_amount").each(function () {
            totalOrderAmount += parseFloat($(this).text().replace(",", "."));
        });
        $('#total_order_amount').text(totalOrderAmount.toFixed(2).replace(".", ","));
        $("#total_price_products").text(totalOrderAmount.toFixed(2).replace(".", ","));
    }

    calculatingBasketAmount();

    $(document).on("change", ".product_amount", function (e) {
        var current_numb = $(this).val();
        var current_tr = $(this).closest("tr");
        var current_price = parseFloat(current_tr.find(".product_price").text().replace(",", ".")).toFixed(2);
        var current_filter = current_tr.find(".hidden").val();
        var total_amount = parseFloat(current_numb * current_price).toFixed(2);
        var url = $("form[name='order']").attr("action");
        var data = {};
        data.numb = current_numb;
        data.filter_id = current_filter;
        data["csrfmiddlewaretoken"] = $('#csrf').children()[0].value;
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            success: function (data) {
                // console.log("OK");
                $("#basket-total-numb").text("(" + data.products.length + ")");
                $(".basket-items ul").html("");
                //v-элемент списка(словарь)
                // {#products попадает из контроллера basket_adding это список словарей, в котором мы проходим по каждому словарю#}
                $.each(data.products, function (k, v) {
                    $(".basket-items ul").append('<li><a style="text-decoration: none;" href="/filters/filter_card/' + v.id + '" title="filter_article filter_name filter_brand">' + v.article + " " + v.name + " " + v.numb + " шт. x " + v.price_per_item + " <I class=\"fa fa-rub\"></I> " + " = " + v.total_price + ' <I class="fa fa-rub"></I><a style="text-decoration: none;" class="delete-item" href="" data-filter_id="' + v.id + '"> <i class="fa fa-times" aria-hidden="true"></i></a></a></li>');
                });
                $(".basket-items ul").append('<li>Итого: ' + data.total_price_all_products + ' <I class="fa fa-rub"></I></li>');

            },
            error: function () {
                console.log("error");
            }
        });
        current_tr.find(".total_product_in_basket_amount").text(total_amount.replace(".", ","));
        calculatingBasketAmount();
    });


    $(document).on("click", "#del_selected", function () {
        // var checked_filters = [];
        var checkbox_list = $(".checkbox");
        var filter_id_list = [];
        $.each(checkbox_list, function (_, checkbox) {
            if (checkbox.checked) {
                var current_tr = $(checkbox).closest("tr");
                filter_id_list.push(current_tr.find("input[type=hidden]").val());
                // checked_filters.push(checkbox);
            }
        });
        var url = $("form[name='order']").attr("action");
        var data = {};
        data.filter_id_list = filter_id_list;
        data.is_delete = true;
        data["csrfmiddlewaretoken"] = $('#csrf').children()[0].value;
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            success: function (data) {
                $("#cart_body").html("");
                $("#basket-total-numb").text("(" + data.products.length + ")");
                $.each(data.products, function () {
                    $(".basket-items ul").html("");
                    //v-элемент списка(словарь)
                    // {#products попадает из контроллера basket_adding это список словарей, в котором мы проходим по каждому словарю#}
                    $.each(data.products, function (k, v) {
                        $(".basket-items ul").append('<li><a style="text-decoration: none;" href="/filters/filter_card/' + v.id + '" title="filter_article filter_name filter_brand">' + v.article + " " + v.name + " " + v.numb + " шт. x " + v.price_per_item + " <I class=\"fa fa-rub\"></I> " + " = " + v.total_price + ' <I class="fa fa-rub"></I><a style="text-decoration: none;" class="delete-item" href="" data-filter_id="' + v.id + '"> <i class="fa fa-times" aria-hidden="true"></i></a></a></li>');
                    });
                    $(".basket-items ul").append('<li>Итого: ' + data.total_price_all_products + ' <I class="fa fa-rub"></I></li>');
                });
                $.each(data.products, function (k, v) {
                    $("#cart_body").append('<tr> <td><p>' + v.article + ' ' + v.name + '</p>' + '<input type="hidden" value="' + v.id + '" class="hidden"></td><td><span class="product_price">' + v.price_per_item + '</span></td><td><input class="w-50 product_amount" type="number" value="' + v.numb + '" min="1" step="1" name="product_in_bascket_"></td><td><span class="total_product_in_basket_amount">' + v.total_price + '</span></td><td><input type="checkbox" name="is_del" class="checkbox"></td></tr>')
                });
                calculatingBasketAmount();
            },
            error: function () {
            }
        })
    });

    $(document).on("click", "#clear_all", function () {
        var url = $("form[name='order']").attr("action");
        data = {};
        data.delete_all = true;
        data["csrfmiddlewaretoken"] = $('#csrf').children()[0].value;
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            success: function (data) {
                $("#cart_body").html("");
                $("#basket-total-numb").text("(" + data.products.length + ")");
                $(".basket-items ul").html("");
                $(".basket-items ul").append('<li>Итого: 0,00 <I class="fa fa-rub"></I></li>');
                calculatingBasketAmount();
            },
            error: function () {
            }
        })
    });


    $(document).on("click", ".delete-item", function (e) {
        e.preventDefault();
        var filter_id = $(this).data("filter_id");
        var filter_article = $(this).data("filter_article");
        var filter_name = $(this).data("filter_name");
        var filter_brand = $(this).data("filter_brand");
        var filter_price = $(this).data("filter_price");
        var numb = 0;
        //{#$(this).closest("li").remove();#}
        basketUpdating(filter_id, filter_article, filter_name, filter_brand, filter_price, numb, is_delete = true)
    });
});