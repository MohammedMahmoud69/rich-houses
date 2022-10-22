from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from captcha.fields import ReCaptchaField

# Contact Data Base

class Contact(models.Model):
    name = models.CharField(max_length=150) # coulmn name
    email = models.EmailField() # coulmn email
    phone_number = PhoneNumberField(null=False , blank=False) # coulmn phone number
    date = models.DateTimeField(auto_now=True) # coulmn date
    subject = models.TextField() # coulmn subject

    # str method
    def __str__(self):
        return self.name
