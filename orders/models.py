from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# order situation choices
SITUATION = (
    ('It was received','It was received'),
    ('In delivery','In delivery'),
    ('In manufacturing','In manufacturing'),
)


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE) # coulmn user
    product = models.CharField(max_length=200) # coulmn product
    quantity = models.IntegerField() # coulmn quantity
    price = models.FloatField() # coulmn price
    city = models.TextField() # coulmn city
    address = models.TextField() # coulmn address
    zip = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(5)]) # coulmn zip code 
    date = models.DateTimeField(auto_now=True) # coulmn date
    situation = models.CharField(max_length=200 , choices=SITUATION , null=True , blank=True) # coulmn situuation
    image = models.ImageField(upload_to="images/orders/" , null=False , blank=False, default='images/default.png') # coulmn image

    # str method
    def __str__(self):
        return str(self.user)