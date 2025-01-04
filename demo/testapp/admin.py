from django.contrib import admin
from .models import TodoItem, TodoItem2, musicProfile

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TodoItem2)
admin.site.register(musicProfile)