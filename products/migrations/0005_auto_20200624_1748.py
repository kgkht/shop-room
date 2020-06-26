# Generated by Django 2.2 on 2020-06-24 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200624_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimages',
            old_name='item',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='price',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 48, 8, 477353)),
        ),
    ]
