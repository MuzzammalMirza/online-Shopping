# Generated by Django 3.2.8 on 2021-11-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20211120_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
