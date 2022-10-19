from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
import qrcode
from io import BytesIO
from PIL import Image , ImageDraw
from django.core.files import File
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Full_Name = models.CharField(max_length=100)
    Phone_Number = PhoneNumberField()
    Date = models.DateTimeField(default=datetime.now , blank=True , null=True)
    qr_code = models.ImageField(upload_to='images/profiles/qr_codes' , default='image/default.jpg' , blank=True , null=True)
    
    # str method
    def __str__(self):
        return str(self.user)


    # edit on save method for qr_code
    def save(self , *args , **kwargs):
        qr_code = qrcode.make(self.user)
        img = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(img)
        img.paste(qr_code)
        fname = f'qr_code-{self.user}'+'.png'
        buffer = BytesIO()
        img.save(buffer,'PNG')
        self.qr_code.save(fname , File(buffer) , save=False)
        img.close()
        super().save(*args , **kwargs)
