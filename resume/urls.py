from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^resume$', views.resume_list, name='resume_list'),
	url(r'^$', views.home, name='home')
]
