from django.db import models

# About us Data Base

class AboutUs(models.Model):
    title = models.CharField(max_length=150) # coulmn title
    subject = models.TextField() # coulmn subject
    image = models.ImageField(upload_to='images/about_us', default='images/default.jpg') # coulmn image
    class Meta:
        verbose_name_plural = "About us"

    # str method
    def __str__(self):
        return self.title