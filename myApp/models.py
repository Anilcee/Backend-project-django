from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Team(models.Model):
    name=models.CharField( max_length=50)
    role=models.CharField( max_length=50)
    image=models.ImageField( upload_to='images/teamimages')
    def __str__(self):
        return self.name

class PetGallery(models.Model):
    petimage=models.ImageField(upload_to='images/petimages')

class OurServices(models.Model):
    serviceName= models.CharField(max_length=30)
    serviceDesc=models.CharField( max_length=200,null=True)
    serviceIcon=models.ImageField(upload_to='images/serviceimages',null=True)
    serviceSubHead=models.TextField(null=True)
    serviceDetails=models.TextField(null=True)
    serviceImage=models.ImageField(upload_to='images/serviceimages',null=True)

class CustomUser(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profilePic = models.ImageField(upload_to="images/profilePic")

class Pets(models.Model):
    petName=models.CharField(max_length=30)
    Breed=models.CharField(max_length=30)
    age=models.CharField(max_length=10)
    image=models.ImageField(upload_to='images/petimages',null=True)
    def __str__(self):
        return self.petName

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.text

class HomeSlide(models.Model):
    image=models.ImageField(upload_to='images/slide')
    title=models.CharField( max_length=30)
    subTitle=models.CharField( max_length=30)
    text=models.CharField( max_length=80)

