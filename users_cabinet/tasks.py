from celery import shared_task

from users.models import Users
from users_cabinet.models import *

from users_cabinet.utils.token import get_token
from users_cabinet.utils.reviews import get_reviews
from users_cabinet.utils.parser import ProductId, ProductSKU


@shared_task
def new_token(login: str, password: str) -> str | None:
    token = get_token(login, password)
    user = Users.objects.get(login_ke=login)
    if token:
        user.login_valid = True
        user.token = token
    else:
        user.login_valid = False
    user.save()
    return token


@shared_task
def review_manager(token, user_pk) -> bool:
    reviews = get_reviews(token)
    user = Users.objects.get(pk=user_pk)
    if reviews:
        for review in reviews:
            Reviews.objects.update_or_create(
                review_id=review['review_id'],
                defaults={
                    'store': review['store'],
                    'product': review['product'],
                    'content': review['content'],
                    'rating': review['rating'],
                    'date_create': review['date_create'],
                    'user': user,
                }
            )
        return True
    return False


@shared_task
def parser(store_name: str, user_pk: str):
    url = 'https://kazanexpress.ru/' + store_name
    product_ids = ProductId(url)
    sku_data = ProductSKU()
    user = Users.objects.get(pk=user_pk)
    store = Stores.objects.get(store_url=url)
    for product_id_set in product_ids.get_product_id():
        for product_id in product_id_set:
            for sku_tuple in sku_data.get_product_data(product_id):
                product_name, price, available, rating, params = sku_tuple[:5]
                param1 = params[0] if params else None
                param2 = params[1] if len(params) > 1 else None

                ProductData.objects.create(
                    product=product_name,
                    price=price,
                    stock_balance=available,
                    url=f'https://kazanexpress.ru/product/{product_id}',
                    rating=rating if rating else None,
                    param1=param1,
                    param2=param2,
                    user=user,
                    store=store
                )


@shared_task
def parser_manager(action: str, store_id: str, token: str):
    if action == 'play':
        ...
    else:
        ...
