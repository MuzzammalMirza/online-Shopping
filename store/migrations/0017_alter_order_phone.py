# Generated by Django 3.2.8 on 2021-11-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]