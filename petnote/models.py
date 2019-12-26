from django.db import models

# Create your models here.

class Pets(models.Model):
            petname=models.CharField(max_length=30)
            img=models.ImageField(upload_to='pics/')
            category=models.CharField(max_length=10)
            price=models.IntegerField()
            adpt=models.BooleanField(default=False)
