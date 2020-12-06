from django.http import JsonResponse
from django.shortcuts import render
from .models import ProductBasket

def basket_add(request):
    return_dict = dict()
    session_key=request.session.session_key
    print(request.POST)
    data=request.POST
    product_id = data.get("product_id")

    new_product, created = ProductBasket.objects.update_or_create(session_key=session_key, product_id=product_id)

    basket_products = ProductBasket.objects.filter(session_key=session_key, is_active=True)
    total_nmb = basket_products.count()
    return_dict["total_nmb"] = total_nmb
    return_dict['products'] = list()

    for item in basket_products:
        product_dict=dict()
        product_dict['name'] = item.product.product_name
        product_dict['price'] = item.product.product_price
        return_dict['products'].append(product_dict)
    return JsonResponse(return_dict)