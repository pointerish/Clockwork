from django.urls import reverse, resolve
from django.test import TestCase


class TestMovieURLs(TestCase):
    """Test URL patterns for movies app."""
    fixtures = ['movie.json']

    def test_urls(self):
        self.assertEqual(reverse('movies:index'), '/movies/')
        self.assertEqual(reverse('movies:detail', kwargs={'id': '1'}), '/movies/1/')
        self.assertEqual(reverse('movies:create'), '/movies/create/')
        self.assertEqual(reverse('movies:update', kwargs={'id': '1'}), '/movies/update/1/')
        self.assertEqual(reverse('movies:delete', kwargs={'id': '1'}), '/movies/delete/1/')
        self.assertEqual(resolve('/movies/').view_name, 'movies:index')
        self.assertEqual(resolve('/movies/1/').view_name, 'movies:detail')
        self.assertEqual(resolve('/movies/create/').view_name, 'movies:create')
        self.assertEqual(resolve('/movies/update/1/').view_name, 'movies:update')
        self.assertEqual(resolve('/movies/delete/1/').view_name, 'movies:delete')
