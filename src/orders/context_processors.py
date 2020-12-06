from .models import ProductBasket


def basket_info_func(request):
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()
    basket_products = ProductBasket.objects.filter(
        session_key=session_key, is_active=True
    )
    if basket_products.count():
        total_nmb = basket_products.count()
    else:
        total_nmb = 0
    return locals()
