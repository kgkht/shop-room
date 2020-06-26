# Generated by Django 2.2 on 2020-06-23 12:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category Name eg(TolyMoly).', max_length=100)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model_number', models.CharField(max_length=100)),
                ('name', models.CharField(help_text='Enter Product Item Name', max_length=200, verbose_name='Title')),
                ('dimension', models.TextField(blank=True, help_text='eg.  1mm x 3mm x 10mm', null=True)),
                ('summary', models.TextField(help_text='Enter Usage or Guideline')),
                ('basic_unit', models.CharField(choices=[('co', 'Count'), ('ft', 'Feet'), ('kg', 'Kilogram'), ('lb', 'Pound'), ('tk', 'Tical')], default='co', help_text='Choice Unit', max_length=2)),
                ('limited', models.BooleanField(help_text='Mark if your product is limited')),
                ('active_for_sale', models.BooleanField(default=True, help_text='if not available, Remove mark!', verbose_name='Can Sale')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Warehouse Name')),
                ('address', models.TextField(help_text='Enter WareHouse Address')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category Name eg(TolyMoly).', max_length=100)),
                ('info', models.TextField()),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.MainCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('last_update', models.DateField()),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, help_text='Product Featured Image (show in most places (200 x 200)px ).', null=True, upload_to='images/featured/')),
                ('image1', models.ImageField(blank=True, help_text='Product Gallery Images', null=True, upload_to='images/products/')),
                ('image2', models.ImageField(blank=True, help_text='Product Gallery Images', null=True, upload_to='images/products/')),
                ('image3', models.ImageField(blank=True, help_text='Product Gallery Images', null=True, upload_to='images/products/')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='products.SubCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Warehouse'),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Lowest Price')),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Normal Price')),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tenth_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='10x Price')),
                ('last_update_time', models.TimeField()),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
    ]