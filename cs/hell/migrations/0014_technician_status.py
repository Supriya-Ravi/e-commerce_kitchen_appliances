# Generated by Django 3.0.3 on 2020-05-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hell', '0013_technician'),
    ]

    operations = [
        migrations.AddField(
            model_name='technician',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
