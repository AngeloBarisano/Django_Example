from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# create a view --> URLs triggers a view

rooms = [
    {"id": 1, "name": "Lets learn python!"},
    {"id": 1, "name": "Design With me"},
    {"id": 1, "name": "Front End dev"},
]


def home(request):
    """The request object is the http object; the request object send
    , what the user sends etc"""
    # return HttpResponse("Home Page")
    context = {"rooms": rooms}
    return render(request, "home.html", context)


def room(request):
    """Return a specific view for rooms using function based views"""
    # return HttpResponse("ROOM")
    return render(request, "room.html")
