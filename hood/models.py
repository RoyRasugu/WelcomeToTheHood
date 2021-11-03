from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pics/',blank=True)
    bio = models.TextField()
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/',blank=True)
    location = models.CharField(max_length=100)
    occupants = models.IntegerField(null=True,default=0)

class Business(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    contact = models.IntegerField()
    
    def __str__(self):
        return self.name

class Police(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address =models.CharField(max_length=100)
    neighbourhood = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/', blank=True)
    
    def __str__(self):
        return self.name

class Health(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='photos/', blank=True)
    address =models.CharField(max_length=100)
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    neigbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.title


