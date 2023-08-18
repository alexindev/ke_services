# Generated by Django 4.2.4 on 2023-08-16 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_id', models.PositiveIntegerField()),
                ('product', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(default=0)),
                ('stock_balance', models.PositiveIntegerField(null=True)),
                ('url', models.CharField(max_length=100)),
                ('rating', models.FloatField(null=True)),
                ('param1', models.CharField(blank=True, max_length=50, null=True)),
                ('param2', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'SKU',
                'verbose_name_plural': 'Все SKU',
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('store_url', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'Все магазины',
            },
        ),
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_1', models.PositiveSmallIntegerField(null=True)),
                ('sales_2', models.PositiveSmallIntegerField(null=True)),
                ('sales_3', models.PositiveSmallIntegerField(null=True)),
                ('sales_4', models.PositiveSmallIntegerField(null=True)),
                ('sales_5', models.PositiveSmallIntegerField(null=True)),
                ('sales_6', models.PositiveSmallIntegerField(null=True)),
                ('sales_7', models.PositiveSmallIntegerField(null=True)),
                ('sku_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_cabinet.productdata')),
            ],
            options={
                'verbose_name': 'продажи',
                'verbose_name_plural': 'Продажи',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=200)),
                ('content', models.TextField(null=True)),
                ('rating', models.PositiveSmallIntegerField(null=True)),
                ('review_id', models.PositiveIntegerField()),
                ('date_create', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='productdata',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_cabinet.stores'),
        ),
        migrations.AddField(
            model_name='productdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
