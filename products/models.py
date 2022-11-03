from django.db import models
from django.utils.text import slugify


# Product Data Base
class Product(models.Model):
    name = models.CharField(max_length=50 , unique=True) # coulmn name
    image = models.ImageField(upload_to="images/products/" , null=False , blank=False, default='images/default.png') # coulmn image
    description = models.TextField(max_length=2000) # coulmn description
    price = models.FloatField() # coulmn price
    date = models.DateField(auto_now_add=True) # coulmn date
    category = models.ForeignKey('Categories' , on_delete = models.CASCADE , null=True , blank=True , default="All") # coulmn category
    slug = models.SlugField(null=True , blank=True , unique=True) # coulmn slug

    # edit on save method and generate the slug
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args , **kwargs)

    # str method
    def __str__(self):
        return self.name



# Category Data Base
class Categories(models.Model):
    Title = models.CharField(max_length=50 , null=False , blank=False)
    class Meta:
        verbose_name_plural = "Categories"

    #str method
    def __str__(self):
        return self.Title
