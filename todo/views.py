from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
  template_name = 'todo-list.html'
  model = Todo
  
class TodoDetailView(DetailView):
  template_name = 'todo-detail.html'
  model = Todo
  
class TodoCreateView(CreateView):
  template_name = 'todo-create.html'
  model = Todo
  fields = ['title', 'body', 'author']
  
class TodoUpdateView(UpdateView):
  template_name = 'todo-update.html'
  model = Todo
  fields = ['id', 'title', 'body', 'author']
  
class TodoDeleteView(DeleteView):
  template_name = 'todo-delete.html'
  model = Todo
  success_url = reverse_lazy('todo_list')