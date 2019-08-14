from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    ongoing = models.BooleanField(blank=False, default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name