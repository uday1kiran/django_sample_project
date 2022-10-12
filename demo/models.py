from django.db import models

# Create your models here.
class Book(models.Model):
 '''STATUSES = (
  (0,'Unknown'),
  (1,'processed'),
  (1, 'paid')
 )'''
 ## title = models.CharField(blank=False, null=True, unique=True, default='', choices=STATUSES) ## if blank is False, null won't be true anyway
 title = models.CharField(max_length=36, blank=False, unique=True)
 description = models.TextField(max_length=256,blank=True)
 price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
 published = models.DateField(blank=True, null=True)
 is_published = models.BooleanField(default=False)
 cover=models.ImageField(upload_to='covers/', blank=True)  ## pip install Pillow , to support image uplaods
 def __str__(self):
   return self.title
 ## more details about fields and field types
 # https://docs.djangoproject.com/en/4.1/ref/models/fields/