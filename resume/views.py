# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Resume
# Create your views here.
depts = ['Engineering', 'People', 'Data Science', 'Services', 'Commercial', 'Finance', 'Global Business Operations']
depts.sort()

def resume_list(request):
	print("lesgitit")
	return render(request, 'resume/resume_list.html', {})

def upload_resume(request):
	return render(request, 'resume/upload_resume.html', {'depts' : depts})


def upload(request):
	new_entry = Resume(old_resume = request.FILES['up_res'], dept=request.POST['dept'], extra=request.POST['extra'])
	new_entry.save()
	print "File name: ", new_entry.old_resume.name
	print "Dept: ", new_entry.dept
	print "Primary key: ", new_entry.pk
	print "hi"
	return render(request, 'resume/upload_resume.html', {'depts': depts})