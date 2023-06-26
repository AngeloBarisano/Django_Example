from django.db import models
from django.contrib.auth.models import User #default user


# Create your models (database classes) here.
# Each class is a table and each attribute is an attribute.
# python manage.py makemigrations 
# python manage.py migrate   

# CRUD: CREATE READ UPDATE DELETE

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    """Inherit from models creating a default id
    
    for custom id you can speficy a uuid manually
    """
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True) # a topic can have multiple rooms but one room can only have one topic
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True) # by setting null == True this means that the database CAN have an instance of this table/ relation with a null value for this relation
    # participants
    updated = models.DateTimeField(auto_now= True) # updates each time
    created = models.DateTimeField(auto_now_add=True) # takes a new snapshot only once



    class Meta:
        ordering = ["-updated", "-created"]
    #create a string representaion of the class
    def __str__(self):
        return self.name




class Message(models.Model):
    """Specify a message which uses a one to many relationship to Room

    Args:
        models (_type_): _description_
    """
    #django has a default user representation such as name, email, superuser, etc
    user = models.ForeignKey(User, on_delete=models.CASCADE) # One to many 
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # if the parent room is deleted all children are deleted
    body = models.TextField() 
    updated = models.DateTimeField(auto_now= True) # updates each time
    created = models.DateTimeField(auto_now_add=True) # takes a new snapshot only once

    def __str__(self):
        return self.body[:50] # only the first 50 characters




