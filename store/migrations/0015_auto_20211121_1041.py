# Generated by Django 3.2.8 on 2021-11-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Availability',
            field=models.CharField(choices=[('In the stock', 'In the stock'), ('out the stock ', 'Out the Stock')], max_length=70, null=True),
        ),
    ]
