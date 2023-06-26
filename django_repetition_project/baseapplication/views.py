from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import RoomForm

# import the models you want to query
"""
To query do essentially:

variable = Model of the name. the objects. and all (all or get, filter, exclude)
queryset= ModelName.objects.all()
"""
from . models import Room


# Create your views here.
# create a view --> URLs triggers a view

# rooms = [
#     {"id": 1, "name": "Lets learn python!"},
#     {"id": 2, "name": "Design With me"},
#     {"id": 3, "name": "Front End dev"},
# ]


def home(request):
    """The request object is the http object; the request object send
    , what the user sends etc"""
    # return HttpResponse("Home Page")
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "baseapplication/home.html", context)


def room(request, pk):
    """Return a specific view for rooms using function based views"""
    # return HttpResponse("ROOM")
    # room = None
    # for i in rooms:
    #     if i["id"] == int(pk):
    #         room = i

    room = Room.objects.get(id = pk)

    context = {"room": room}        

    return render(request, "baseapplication/room.html", context)


def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        # print("test print of name", request.POST.get("name"))
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        print(request.POST)
    context = {"form" : form}
    return render(request, "baseapplication/room_form.html", context)


def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {"form" : form}
    return render(request, "baseapplication/room_form.html", context)



def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "baseapplication/delete.html", {"obj" : room})