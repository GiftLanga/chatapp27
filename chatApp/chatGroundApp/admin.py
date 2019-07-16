from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room, 
  list_display=["name", "label"])
admin.site.register(Message)