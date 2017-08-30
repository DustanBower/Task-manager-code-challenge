# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    "Model to track user tasks (i.e., TODO items)"
    user = models.ForeignKey(User, help_text="User that task is assigned to")
    title = models.CharField(max_length=100, help_text="Title of task")
    description = models.TextField(help_text="Description of task")

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
