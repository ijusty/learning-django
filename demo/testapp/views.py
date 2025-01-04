from django.shortcuts import render, HttpResponse
from django.utils.translation import gettext_lazy as _
from .models import TodoItem, TodoItem2, musicProfile, Seller

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    items2 = TodoItem2.objects.all()
    items3 = musicProfile.objects.all()
    sellers = Seller.objects.all()

    

    
    return render(request, "todos.html", {"todos": items, "todos2": items2, "musics": items3})


def sellers(request):
    sellers = Seller.objects.all()

    grouped_sellers = {}
    for seller in sellers:
        year = seller.year_in_university
        if year not in grouped_sellers:
            grouped_sellers[year] = []
        grouped_sellers[year].append(seller)

    return render(request, "sellers.html", {"grouped_sellers": grouped_sellers})

def playlists(request):
    items3 = musicProfile.objects.all()

    

    
    return render(request, "playlists.html", {"musics": items3})