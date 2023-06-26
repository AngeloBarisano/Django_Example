"""Create App-specific urls (different from django baseline urls framework)


"""


from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:pk>", views.room, name="room"), # as long as you call it name = "room", you can change all names etcd
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
        path("delete-room/<str:pk>/", views.deleteRoom, name="delete-room"),

]
