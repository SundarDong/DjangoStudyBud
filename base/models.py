from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
def __str__(self):
    return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null= True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-updated','-created']
        #When we add minus(-) in the above then it will shows the data from recent data to old data

    def __str__(self):
        return self.name

class Message(models.Model):
    #user model is prebuild model in django framework.
    user = models. ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #If main parent delete then the child also delete.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.body[0.50]
