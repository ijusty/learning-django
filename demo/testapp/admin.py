from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import TodoItem, TodoItem2, musicProfile, Seller

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TodoItem2)
admin.site.register(musicProfile)
admin.site.register(Seller)