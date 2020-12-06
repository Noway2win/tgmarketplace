from .models import ProductBasket


def basket_info_func(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    basket_products = ProductBasket.objects.filter(
        session_key=session_key, is_active=True
    )
    total_nmb = basket_products.count()

    return locals()
