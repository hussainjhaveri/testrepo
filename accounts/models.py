from django.contrib.auth.models import User
from django.db import models
types = [('dog','dog'),('cat','cat'),('bird','bird')]

class Pets(models.Model):
    name = models.CharField(max_length=100,null= False)
    species = models.CharField(max_length=10, choices=types )
    age = models.IntegerField()
    owner = models.ForeignKey(User,on_delete= models.CASCADE )