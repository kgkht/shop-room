from django.db import models
from datetime import datetime
# Create your models here.
from django.urls import reverse
from django.http import HttpResponseRedirect


class SiteSettings(models.Model):
    logo = models.ImageField(upload_to="images/",null=True, blank=True, help_text="Upload Your Shop Logo.")
    name = models.CharField(max_length=250, help_text='Enter Your Shop Name')
    description = models.TextField(help_text="Shop Description (max:250 words).")
    keywords = models.CharField(max_length=250, help_text="Keywords seperate with comma, eg(Electric Shop, Myanmar Electric, Shop).")

   
    phone = models.CharField(max_length=50, help_text="Enter Phone Number")
    email = models.EmailField(max_length=150, help_text="Enter Email Address")
    address = models.TextField(help_text="Enter Shop Address")
    since = models.DateField(default=datetime.now().year,help_text="Enter Since Year")
    cpright = models.CharField('Copyright',max_length=200, help_text="Enter Copyright Text")
    
    
    author = models.CharField(max_length=150, help_text="Enter App Developer Name")


    def short_desb(self):
        return self.description[:75]

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('dashboard:site-settings', args=[str(self.id)])
