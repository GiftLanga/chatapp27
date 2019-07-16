from . import views
from django.conf.urls import url

urlpatterns = (
  url(r'^login/$', views.loginUser, name='login'),
  url(r'^register/$', views.register, name='register'),
  url(r'^logout/$', views.logoutUser, name='logout'),
)