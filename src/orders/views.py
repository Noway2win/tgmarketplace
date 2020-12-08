from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from .forms import ConfirmationForm
from .models import ProductBasket, ProductOrder, Order


def basket_add(request):
    try:
        return_dict = dict()
        session_key = request.session.session_key
        print(request.POST)
        data = request.POST
        product_id = data.get("product_id")
        is_delete = data.get("is_delete")
        if is_delete == 'true':
            ProductBasket.objects.filter(id=product_id).update(is_active=False)
        else:
            new_product, created = ProductBasket.objects.update_or_create(
                session_key=session_key, product_id=product_id, is_active=True,
            )

        basket_products = ProductBasket.objects.filter(
            session_key=session_key, is_active=True
        )
        total_nmb = basket_products.count()
        return_dict["total_nmb"] = total_nmb
        return_dict["products"] = list()

        for item in basket_products:
            product_dict = dict()
            product_dict["id"] = item.id
            product_dict["name"] = item.product.product_name
            product_dict["price"] = item.product.product_price
            return_dict["products"].append(product_dict)
            print(return_dict)
    except:
        return_dict = dict()
    return JsonResponse(return_dict)

# def confirmation(request):
#     return_dict = dict()
#     session_key = request.session.session_key
#     products_in_basket= ProductBasket.objects.filter(session_key=session_key, is_active=True)
#     product_prices = list()
#     for item in products_in_basket:
#         product_prices.append(item.product.product_price)
#
#     total_price = sum(product_prices)
#     form = ConfirmationForm(request.POST or None)
#     if request.POST:
#         print(request.POST)
#         if form.is_valid():
#             print('ok')
#             data=request.POST
#             user = request.user
#             name = data.get('name')
#             message = data.get('message')
#             address=data.get('address')
#             phone = data.get('phone')
#         # ПОЛЬЗОВАТЕЛЬ
# #                .
# #             .
# #             .
# # .
#
#             if not request.user.is_authenticated:
#                 user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})
#
#
#             order = Order.objects.create(user=user, customer_name=name, phone=phone, extra_message=message, customer_address=address)
#
#             for name, value in data.items():
#                 if name.startswith("product_in_basket_"):
#                     basket_prod_id=name.split("product_in_basket_")[1]
#                     basket_product = ProductBasket.objects.get(id=basket_prod_id)
#                     product = basket_product.product
#                     ProductOrder.objects.create(product=product, price=ProductBasket.price, order=order)
#
#
#         else:
#             print('no')
#     return render(request, 'products/order_form.html', locals())

def confirmation(request):
    try:
        return_dict = dict()
        session_key = request.session.session_key
        products_in_basket= ProductBasket.objects.filter(session_key=session_key, is_active=True)
        product_prices = list()
        for item in products_in_basket:
            product_prices.append(item.product.product_price)

        total_price = sum(product_prices)
        form = ConfirmationForm(request.POST or None)
        if request.POST:
            print(request.POST)
            if form.is_valid():
                print('ok')

                data=request.POST
                phone = data.get('phone')
                name = data.get('name')
                message = data.get('message')
                address=data.get('address')
                if not request.user.is_authenticated:
                    user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})
                    order = Order.objects.create(user=user, customer_name=name, phone=phone, extra_message=message, customer_address=address)
                else:
                    user = request.user
                    order = Order.objects.create(user=user, customer_name=name, phone=phone, extra_message=message,
                                                 customer_address=address)
                for name, value in data.items():
                    if name.startswith("product_in_basket_"):
                        basket_prod_id=name.split("product_in_basket_")[1]
                        basket_product = ProductBasket.objects.get(id=basket_prod_id)
                        product = basket_product.product
                        ProductOrder.objects.create(product=product, price=ProductBasket.price, order=order)


            else:
                print('no')
    except:
        return_dict = dict()
    return render(request, 'products/order_form.html', locals())