from django.contrib import admin

# Register your models here.

from . import models
from dashboard.models import UserProfile

admin.site.register(models.Product)
admin.site.register(models.Price)
admin.site.register(models.Stock)
admin.site.register(models.ProductImages)
admin.site.register(models.MainCategory)
admin.site.register(models.SubCategory)
admin.site.register(models.Warehouse)
admin.site.register(UserProfile)
