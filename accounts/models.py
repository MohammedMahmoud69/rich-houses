from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Profile Data Base


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # coulmn user
    Full_Name = models.CharField(max_length=100) # coulmn name
    Phone_Number = PhoneNumberField() # coulmn phone number
    Date = models.DateTimeField(default=datetime.now , blank=True , null=True) # coulmn date
    
    # str method
    def __str__(self):
        return str(self.user)

