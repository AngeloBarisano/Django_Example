from django.forms import ModelForm
from . models import Room




class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__" # alternative ["name", "body"] # this will create the form based on the meta data on Room model relation






        