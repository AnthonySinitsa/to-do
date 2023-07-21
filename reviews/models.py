from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Review(models.Model):
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  body = models.TextField(default='good product:/')
  
  def __str__(self):
    return self.author
  
  def get_absolute_url(self):
    return reverse('reviews', args=[str(self.id)])