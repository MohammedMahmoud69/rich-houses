from xmlrpc.client import DateTime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import Profile
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

SITUATION = (
    ('It was received','It was received'),
    ('In delivery','In delivery'),
    ('In manufacturing','In manufacturing'),
)


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.FloatField()
    city = models.TextField()
    address = models.TextField()
    zip = models.IntegerField(max_length=7)
    date = models.DateTimeField(auto_now=True)
    situation = models.CharField(max_length=200 , choices=SITUATION , null=True , blank=True)
    image = models.ImageField(upload_to="images/orders/" , null=False , blank=False, default='images/default.png')

    def __str__(self):
        return str(self.user)