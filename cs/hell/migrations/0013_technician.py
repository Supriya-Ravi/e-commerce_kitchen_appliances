# Generated by Django 3.0.3 on 2020-05-30 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hell', '0012_delete_technician'),
    ]

    operations = [
        migrations.CreateModel(
            name='technician',
            fields=[
                ('complaint_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('complaint', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]