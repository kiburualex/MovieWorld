import json
from django.test import TestCase
from .models import Movie

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

# Model Test Case.

class ModelTestCase(TestCase):
    """This class defines the test suite for the movie model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.movie_title = "Code Writer"
        self.movie_description = "Write world class code"
        self.movie = Movie(title=self.movie_title, description=self.movie_description)

    def test_model_can_create_a_movie(self):
        """Test the movie model can create a movie."""
        old_count = Movie.objects.count()
        self.movie.save()
        new_count = Movie.objects.count()
        self.assertNotEqual(old_count, new_count)


# Api Test Case

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        # create sample user
        user = get_user_model().objects.create_user(name='testuser', email='testuser@example.com', password='$helter123*')
        user.is_active = False
        user.save()

        # enforce login using created user credentials
        user = get_user_model().objects.get(email='testuser@example.com')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        users_url = reverse('users:list')
        resp = self.client.get(users_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.movie_data = {'title': 'Go to Ibiza', 'description':'Once upon a time'}
        self.response = self.client.post(
            reverse('movies:create'),
            self.movie_data,
            format="json")

        self.movie = Movie.objects.all().last()

    def test_api_can_create_a_movie(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_movie(self):
        """Test the api can get movies."""
        response = self.client.get(
            reverse('movies:list'),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_movie(self):
        """Test the api can get a given movie."""
        movie = Movie.objects.create(title='Test Movie', description='Awesome movie')
        movie.save()

        response = self.client.get(
            reverse('movies:detail',
            kwargs={'pk': movie.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, movie.title)

    def test_api_can_update_movie(self):
        """Test the api can update a given movie."""
        change_movie = {'title': 'Something new'}
        res = self.client.put(
            reverse('movies:update', kwargs={'pk': self.movie.id}),
            change_movie, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)



    def test_api_can_delete_movie(self):
        """Test the api can delete a movie."""
        movie = Movie.objects.create(title='Test Movie', description='Awesome movie')
        movie.save()
        response = self.client.delete(
            reverse('movies:delete', kwargs={'pk': movie.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)