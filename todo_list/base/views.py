from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .models import Task

class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('tasks')

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
  model = Task 
  context_object_name = "tasks"

class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = "task"  
  template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')  

class DeleteView(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task' 
  success_url = reverse_lazy('tasks') 


def logout_user(request):
    logout(request)

    return redirect('login')  

  