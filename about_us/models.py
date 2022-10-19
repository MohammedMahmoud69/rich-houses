from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    subject = models.TextField()
    image = models.ImageField(upload_to='images/about_us', default='images/default.jpg')

    def __str__(self):
        return self.title