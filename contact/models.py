from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from captcha.fields import ReCaptchaField
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False , blank=False)
    date = models.DateTimeField(auto_now=True)
    subject = models.TextField()
    captcha = ReCaptchaField()

    def __str__(self):
        return self.name
