import uuid
from django.db import models
from datetime import datetime as now_time
from django.urls import reverse_lazy, reverse


class MainCategory(models.Model):
    name = models.CharField(max_length=100, help_text="Category Name eg(TolyMoly).")
    info = models.TextField()
    
    def __str__(self):
        return self.name


    
class SubCategory(models.Model):
    name = models.CharField(max_length=100, help_text="Category Name eg(TolyMoly).")
    info = models.TextField()
    #main_category = models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

    

class Warehouse(models.Model):
    name = models.CharField('Warehouse Name', max_length=100)
    address = models.TextField(help_text="Enter WareHouse Address")

    
    def __str__(self):
        return self.name




class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_number = models.CharField(max_length=100)
    name = models.CharField("Title",
                            max_length=200,
                            help_text="Enter Product Item Name")

    #images = models.ForeignKey('ProductImages', on_delete=models.SET_NULL, null=True)
    
    dimension = models.TextField(blank=True, null=True, help_text="eg.  1mm x 3mm x 10mm")
    summary = models.TextField(help_text="Enter Usage or Guideline")

    unit_choices = (
        ('co', 'Count'),
        ('ft', 'Feet'),
        ('kg', 'Kilogram'),
        ('lb', 'Pound'),
        ('tk', 'Tical'),
    )
    basic_unit = models.CharField(max_length=2,
                                  choices=unit_choices,
                                  default='co',
                                  help_text="Choice Unit")

    category1 = models.ManyToManyField(MainCategory)
    category2 = models.ManyToManyField(SubCategory)


    #stocks = models.ForeignKey('Stock', on_delete=models.CASCADE)
    #prices = models.ForeignKey('Price', on_delete=models.CASCADE, null=True, blank=True)
    

    limited = models.BooleanField(help_text="Mark if your product is limited")
    active_for_sale = models.BooleanField('Can Sale',default=True, help_text="if not available, Remove mark!")

    warehouse = models.ForeignKey('Warehouse', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.model_number)


    def get_absolute_url(self):
        return reverse('dashboard:product-detail', args=[str(self.id)])



class ProductImages(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    featured_image = models.ImageField(upload_to='images/featured/',
                                       null=True,
                                       blank=True,
                                       help_text="Product Featured Image (show in most places (200 x 200)px ).")
    
    image1 = models.ImageField(upload_to='images/products/', null=True, blank=True, help_text="Product Gallery Images")
    
    image2 = models.ImageField(upload_to='images/products/', null=True, blank=True, help_text="Product Gallery Images")
    
    image3 = models.ImageField(upload_to='images/products/', null=True, blank=True, help_text="Product Gallery Images")

    
    def __str__(self):
        return str(self.product_id.name)



class Stock(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    stock = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_id)




class Price(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    low_price = models.DecimalField('Lowest Price', decimal_places=2, max_digits=9)
    normal_price = models.DecimalField('Normal Price', decimal_places=2, max_digits=9)
    base_price = models.DecimalField(decimal_places=2, max_digits=8)
    tenth_price = models.DecimalField('10x Price', decimal_places=2, max_digits=8)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_id)

