# Generated by Django 3.2.8 on 2021-11-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211117_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('subject', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=70)),
            ],
        ),
    ]
