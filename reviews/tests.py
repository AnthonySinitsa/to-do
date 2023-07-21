from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Review

class ReviewTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='reviewuser', email="tester@email.com", password="pass"
    )
    self.review = Review.objects.create(
      name='Harry Potter', author=self.user, review='An excellent review'
    )
    
    def test_string_representation(self):
      review = Review(name='Harry Potter')
      self.assertEqual(str(review), review.name)
      
    def test_review_content(self):
      self.assertEqual(f'{self.review.name}', 'Harry Potter')
      self.asserEqual(f'{self.review.author}', 'reviewuser')
      self.assertEqual(f'{self.review.review}', 'An excellent review')
      
    def test_review_list_view(self):
      response = self.client.get(reverse('review_list'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Harry Potter')
      self.assertTemplateUsed(response, 'reviews-list.html')
      
    