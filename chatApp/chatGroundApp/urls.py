from . import views
from django.conf.urls import url

urlpatterns = [
  url(r'^$', views.chatGroundHome, name='chatGround'),
  url(r'(?P<roomLabel>[\w-]+)/$', views.chatGroundHome, name='chatGroundRoom'),
]