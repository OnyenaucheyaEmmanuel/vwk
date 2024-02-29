# Generated by Django 3.2.6 on 2022-12-26 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_auto_20221226_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 17, 34, 23, 897213)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 17, 34, 23, 901084)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 17, 34, 23, 895228)),
        ),
    ]
