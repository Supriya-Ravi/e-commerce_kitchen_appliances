# Generated by Django 3.0.3 on 2020-03-03 07:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hell', '0002_delete_add_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_items',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
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
