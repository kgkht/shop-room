# Generated by Django 2.2 on 2020-06-24 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200624_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='last_update_time',
            field=models.DateTimeField(default=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]