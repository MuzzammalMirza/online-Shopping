# Generated by Django 3.2.8 on 2021-11-19 10:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/order/')),
                ('product', models.IntegerField(max_length=70)),
                ('quantity', models.CharField(max_length=70)),
                ('price', models.FloatField(max_length=70)),
                ('address', models.TextField(max_length=200)),
                ('phone', models.IntegerField(max_length=20)),
                ('pincode', models.CharField(max_length=70)),
                ('date', models.DateTimeField(default=datetime.date)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
