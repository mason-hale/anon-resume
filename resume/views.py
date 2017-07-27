# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def resume_list(request):
	print("lesgitit")
	return render(request, 'resume/resume_list.html', {})
