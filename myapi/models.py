
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from versatileimagefield.fields import VersatileImageField, PPOIField
class changed(models.Model):
    Battry = models.BooleanField()
    Mic = models.BooleanField()
    Speaker = models.BooleanField()
    Lcd =models.BooleanField()
    Touch= models.BooleanField()
    FrontCam=models.BooleanField()
    BackCam=models.BooleanField()
    other=models.CharField( max_length=256,blank=True)
    def __str__(self):
         return str(self.Battry)
        
class broke(models.Model):
    Battry = models.BooleanField()
    Mic = models.BooleanField()
    Speaker = models.BooleanField()
    Lcd =models.BooleanField()
    Touch= models.BooleanField()
    FrontCam=models.BooleanField()
    BackCam=models.BooleanField()
    other=models.CharField( max_length=256,blank=True)
    def __str__(self):
        return str(self.Battry)
class color(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name      
class mod(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name          
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    mod=models.OneToOneField(mod,on_delete=CASCADE)
    year = models.CharField(max_length=5)
    ram = models.CharField(max_length=5)
    BattryHealth=models.CharField(max_length=2)
    color=models.OneToOneField(color,on_delete=CASCADE)
    Broken=models.OneToOneField(broke,on_delete=CASCADE)
    change=models.OneToOneField(changed,on_delete=CASCADE)
    image = models.ManyToManyField('myapi.Image', related_name='products')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.year
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name