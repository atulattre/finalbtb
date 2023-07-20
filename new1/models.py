from django.db import models
from django.contrib.auth.models import User

#class Image(models.Model):
   # image = models.ImageField(upload_to='images/')

class User1(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    firstname = models.CharField(max_length=100,null=False)
    lastname = models.CharField(max_length=100)
    
    
    student_id=models.IntegerField(default=0)
    phone=models.IntegerField()
    
    branch = models.CharField(max_length=100)
    
    year=models.IntegerField(default=0)
    
   
    building_name = models.CharField(max_length=100)
    
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    space=models.IntegerField(default=0)
    rent = models.CharField(max_length=100)
    
    images1 = models.ImageField(upload_to="media",null=True)
    comments = models.CharField(max_length=255)
    def __str__(self):
        return str(self.username)
