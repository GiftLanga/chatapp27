from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm, UserDetailsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def loginUser(request):
  print "login user"
  if(request.method == "POST"):
    form  = request.POST.dict()
    username = form.get("username")
    password = form.get("password")

    user = authenticate(username=username, password=password)
    if user:
      if user.is_active:
        login(request, user)
        return redirect('/chatGround/')
      else:
        messages.add_message(request, messages.ERROR, 'Your account is not active')
        return redirect('/')
    else:
      messages.add_message(request, messages.ERROR, 'Invalid login details')
      return redirect('/')
  else:
    return redirect('/')

def register(request):
  if request.method == "POST":
    user_details_form = UserDetailsForm(data=request.POST)
    registration_form = RegistrationForm(data=request.POST)

    if user_details_form.is_valid() and registration_form.is_valid():
      user  = user_details_form.save()
      user.set_password(user.password)
      user.save()

      register = registration_form.save(commit=False)
      register.user = user
      register.save()
      return loginUser(request)
    else:
      my_dict = {
        'registrationForm': registration_form,
        'userDetailsForm': user_details_form,
        'loginForm': LoginForm(),
      }
      return render(request, 'home.html', context=my_dict)
  else:
    return redirect('/')

def logoutUser(request):
  if(request.method == "POST"):
    logout(request)
    return redirect('/')
  else:
    return redirect('/')