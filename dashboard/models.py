from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    account_info = models.ForeignKey(User, on_delete=models.CASCADE, help_text="website login account, (not deals with accountant informations).")
    phone = models.CharField(max_length=13, help_text="Phone Number")
    nrc = models.CharField('NRC Number', max_length=18, null=True, blank=True)
    address = models.TextField(help_text="Enter Full Address.")
    salary = models.IntegerField()

    def __str__(self):

       return f"{self.account_info}"
