from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class TaskList(ListView):
  model = Task 
  context_object_name = "tasks"

class TaskDetail(DetailView):
  model = Task
  context_object_name = "task"  
  template_name = 'base/task.html'


class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')  

class DeleteView(DeleteView):
  model = Task
  context_object_name = 'task' 
  success_url = reverse_lazy('tasks') 

  