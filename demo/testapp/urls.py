from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("sellers/", views.sellers, name="sellers"),
    path("playlists/", views.playlists, name="playlists")
]