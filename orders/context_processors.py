def getting_basket_info(request):
    # Текущая сессия, если нет, то создаем
    session_key = request.session.session_key
    if not session_key:
        # workaround for newer Django versions
        request.session["session_key"] = 123
        # re-apply value
        request.session.cycle_key()
        request.session.set_expiry(604800)
        request.session['cart'] = []
    products_in_basket = []
    total_price_all_product = 0.00
    if request.session["cart"]:
        for item in request.session["cart"]:
            item["total_price"] = "{0:.2f}".format(
                float(item["filter_price"].replace(",", ".")) * int(item["numb"])).replace(".", ",")
            products_in_basket.append(item)
            total_price_all_product += float(item["total_price"].replace(",", "."))
    total_price_all_product = "{0:.2f}".format(total_price_all_product).replace(".", ",")
    request.session.modified = True
    # Переменные, которые видны везде
    # Продукты в корзине в этой сессии, активные, чтобы перебирать элементы и выводить их в корзине
    # products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    # Считаем количество этих элементов, чтобы выводить в скобочках около корзины
    products_total_nmb = len(products_in_basket)
    return locals()
