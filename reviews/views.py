from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from django.urls import reverse_lazy

class ReviewListView(ListView):
  template_name = 'review-list.html'
  model = Review
  
class ReviewDetailView(DetailView):
  template_name = 'review-detail.html'
  model = Review
  
class ReviewCreateView(CreateView):
  template_name = 'review-create.html'
  model = Review
  fields = ['title', 'body', 'author']
  
class ReviewUpdateView(UpdateView):
  template_name = 'review-update.html'
  model = Review
  fields = ['id', 'title', 'body', 'author']
  
class ReviewDeleteView(DeleteView):
  template_name = 'review-delete.html'
  model = Review
  success_url = reverse_lazy('review_list')