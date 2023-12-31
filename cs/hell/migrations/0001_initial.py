# Generated by Django 3.0.3 on 2020-02-28 08:03

import datetime
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
            name='categories',
            fields=[
                ('catid', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ordered_items',
            fields=[
                ('order_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('payment_type', models.CharField(max_length=20)),
                ('status', models.CharField(default='Payment pending', max_length=50)),
                ('shipping_status', models.CharField(default='Shipping pending', max_length=300)),
                ('delivery_status', models.CharField(default='Delivery pending', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='useraddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('pno', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpurchase', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='add_items',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('actual_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('image', models.FileField(upload_to='images')),
                ('updated_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(default='not specified')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hell.categories')),
            ],
        ),
    ]
