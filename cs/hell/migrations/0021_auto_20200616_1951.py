# Generated by Django 3.0.3 on 2020-06-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hell', '0020_auto_20200613_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
