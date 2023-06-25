from django.contrib import admin

# Register your models here.

from . models import Room, Topic, Message

# register the model to admin
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)