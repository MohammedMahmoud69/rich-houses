from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils.text import slugify
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image , ImageDraw
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    image = models.ImageField(upload_to="images/products" , null=False , blank=False, default='images/default.png')
    describtion = models.TextField(max_length=2000)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Categories' , on_delete = models.CASCADE , null=True , blank=True , default="All")
    slug = models.SlugField(null=True , blank=True , unique=True)
    qr_code = models.ImageField(upload_to='images/products/qr_codes' , default='image/default.jpg' , blank=True , null=True)
    
    # edit on save method and generate the slug
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args , **kwargs)
    # edit on save method to qrcode
        qrcode_img = qrcode.make(self.name)
        img = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(img)
        img.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        img.save(buffer,'PNG')
        self.qr_code.save(fname , File(buffer) , save=False)
        img.close()
        super().save(*args , **kwargs)

    # str method
    def __str__(self):
        return self.name




class Categories(models.Model):
    Title = models.CharField(max_length=50 , null=False , blank=False)

    #str method
    def __str__(self):
        return self.Title

