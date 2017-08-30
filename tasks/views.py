# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# I don't like importing multiple things on one line because it leads
# to merge conflicts when multiple people are working on different things in
# the same file.  Single line imports merge without incident.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from tasks.models import Task

class TaskCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Task
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Task
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        qs = super(TaskDelete, self).get_queryset().filter(
	    user=self.request.user)
        return qs


class TaskDetail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Task

    def get_queryset(self):
        qs = super(TaskDetail, self).get_queryset().filter(
	    user=self.request.user)
        return qs


class TaskList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Task

    def get_queryset(self):
        qs = super(TaskList, self).get_queryset().filter(
	    user=self.request.user)
        return qs


class TaskUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Task
    fields = ['title', 'description']

    def get_queryset(self):
        qs = super(TaskUpdate, self).get_queryset().filter(
	    user=self.request.user)
        return qs
