from django.conf.urls import url
from . import views

app_name = 'resume'
urlpatterns = [
	url(r'^resume$', views.resume_list, name='resume_list'),
	url(r'upload_resume$', views.upload_resume, name='upload_resume'),
	url(r'upload_old$', views.upload, name='upload'),
]
