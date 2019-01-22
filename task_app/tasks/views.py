from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from . import models

class TaskCreateView(CreateView):
    model = models.Task
    template_name = 'task_new.html'
    fields = ['name']

class TaskListView(ListView):
    model = models.Task
    template_name = 'task_list.html'

class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'task_detail.html'

class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['name']
    template_name = 'task_edit.html'

class TaskDeleteView(DeleteView):
    model = models.Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
