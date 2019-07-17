from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message

# Create your views here.
@login_required
def chatGroundHome(request, roomLabel=None):
  if request.user.is_authenticated:
    rooms = Room.objects.all()
    messages = []
    if roomLabel:
      r = Room.objects.get(label=roomLabel)
      try:
        messages = Message.objects.all().filter(room=r)
      except:
        messages = []
    my_dict = {
      "username": request.user.username,
      "rooms": rooms,
      "messages": messages,
    }

    return render(request, 'chatGround/chatGround.html', context=my_dict)
  else:
    return redirect('/')
