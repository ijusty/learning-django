from django.shortcuts import render, HttpResponse
from .models import TodoItem, TodoItem2, musicProfile

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    items2 = TodoItem2.objects.all()
    items3 = musicProfile.objects.all()
    return render(request, "todos.html", {"todos": items, "todos2": items2, "musics": items3})
