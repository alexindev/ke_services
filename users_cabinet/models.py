from django.db import models

from users.models import Users


class UserStores(models.Model):
    store_name = models.CharField(max_length=50)
    product = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    sale = models.PositiveIntegerField(default=0)
    stock_balance = models.PositiveIntegerField(default=0)
    url = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    param1 = models.CharField(max_length=50, blank=True)
    param2 = models.CharField(max_length=50, blank=True)
    datetime = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    store = models.ForeignKey('Stores', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'Детализация по магазинам'

    def __str__(self):
        return str(self.store)

class Stores(models.Model):
    name = models.CharField(max_length=50)
    store_url = models.CharField(max_length=100)
    users = models.ManyToManyField(Users, through='UserStores')

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'Все магазины'

    def __str__(self):
        return self.name


class Reviews(models.Model):
    store = models.CharField(max_length=50)
    product = models.CharField(max_length=200)
    text_review = models.TextField(blank=True)
    rating = models.SmallIntegerField()
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.product

