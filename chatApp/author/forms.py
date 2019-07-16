from django import forms
from author.models import UserDetails
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
  class Meta():
    model = User
    fields = ('username', 'password',)
    widgets = {
      'username': forms.TextInput(attrs = {'placeholder': 'Username'}),
      'password': forms.PasswordInput(attrs = {'placeholder': 'Password'})
    }

class UserDetailsForm(forms.ModelForm):
  confirm_password = forms.CharField(label='Confirm Password', widget =
      forms.PasswordInput(attrs = {'placeholder': 'Confirm Password'}),
    )
  class Meta():
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password',)
    widgets = {
      'first_name': forms.TextInput(attrs = {'placeholder': 'First name'}),
      'last_name': forms.TextInput(attrs = {'placeholder': 'Last name'}),
      'username': forms.TextInput(attrs = {'placeholder': 'Username'}),
      'email': forms.TextInput(attrs = {'placeholder': 'E-mail'}),
      'password': forms.TextInput(attrs = {'placeholder': 'Password'}),
    }

class RegistrationForm(forms.ModelForm):
  class Meta():
    model = UserDetails
    fields = ( 'gender',)
    widgets = {
      'gender': forms.Select(attrs={'placeholder': 'Gender'}, choices=[
          ('Male', 'Male'), 
          ('Female', 'Female'),
          ('Other', 'Other'),])
    }
