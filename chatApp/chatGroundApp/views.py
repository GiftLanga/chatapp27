from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room

# Create your views here.
@login_required
def chatGroundHome(request):
  if request.user.is_authenticated:
    rooms = Room.objects.all()
    my_dict = {
      "username": request.user.username,
      "rooms": rooms,
    }

    return render(request, 'chatGround/chatGround.html', context=my_dict)
  else:
    return redirect('/')
