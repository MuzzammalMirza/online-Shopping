# Generated by Django 3.2.8 on 2021-11-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_order_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(upload_to='ecommerce/pimg/'),
        ),
    ]
