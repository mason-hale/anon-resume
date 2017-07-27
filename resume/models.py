# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Resume(models.Model):
     old_resume = models.ImageField(upload_to='old_resumes/')
     new_resume = models.ImageField(upload_to='new_resumes/')
     dept = models.TextField(max_length=20)
     extra = models.TextField(max_length=40)
