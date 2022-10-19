from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/blog')
    date = models.DateTimeField(default=datetime.now())
    description = models.TextField(max_length=5000)
    category  = models.ForeignKey('Category' , on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title