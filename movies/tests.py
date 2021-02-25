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
        self.client = APIClient()
        # create sample user
        user = get_user_model().objects.create_user(name='testuser', email='testuser@example.com', password='$helter123*')
        user.is_active = False
        user.save()
            
        # login to the jwt with created user details
        auth_url = reverse('jwt-auth')
        resp = self.client.post(auth_url, {'email':'admin@example.com', 'password':'$helter123*'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('token' in resp.data)
        self.token = resp.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))

        # self.client.login(username='admin@example.com', password='$helter123*')
        self.movie_data = {'title': 'Go to Ibiza', description:'Once upon a time'}
        self.response = self.client.post(
            reverse('movies:create'),
            self.movie_data,
            format="json")

    def test_api_can_create_a_movie(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_movie(self):
        """Test the api can get a given movie."""
        movie = movie.objects.all().last()
        response = self.client.get(
            reverse('movies:details',
            kwargs={'pk': movie.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, movie)

    def test_api_can_update_movie(self):
        """Test the api can update a given movie."""
        change_movie = {'title': 'Something new'}
        movie = movie.objects.all().last()
        res = self.client.put(
            reverse('movies:details', kwargs={'pk': movie.id}),
            change_movie, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_movie(self):
        """Test the api can delete a movie."""
        movie = movie.objects.all().last()
        response = self.client.delete(
            reverse('movies:details', kwargs={'pk': movie.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)