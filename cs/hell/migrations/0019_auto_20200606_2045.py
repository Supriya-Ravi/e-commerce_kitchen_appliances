# Generated by Django 3.0.3 on 2020-06-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hell', '0018_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1),
        ),
    ]
