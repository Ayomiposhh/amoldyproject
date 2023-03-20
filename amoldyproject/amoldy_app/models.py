from email.mime import image
from django.db import models


# Create your models here.


class Contact(models.Model):
  name= models.CharField(max_length= 100,null=True,blank=True)
  email=models.EmailField()
  message=models.TextField()

  def __str__(self): 
    return self.name
  
class Categories(models.Model):
  name= models.CharField(max_length= 100,null=True,blank=True)
  
  
class Shop(models.Model):
  name= models.CharField(max_length= 100,null=True,blank=True)
  image= models.ImageField()
  price= models.IntegerField(null=True)
  
  def __str__(self): 
    return self.name
  
  