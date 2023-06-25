"""Create App-specific urls (different from django baseline urls framework)


"""


from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("room/", views.room, name="room"),
]
