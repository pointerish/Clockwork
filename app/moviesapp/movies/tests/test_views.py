from django.test import TestCase

from moviesapp.movies.models import Movie


class TestMovieViews(TestCase):
    
    def setUp(self):
        Movie.objects.create(
            pk='8',
            title='Tight Deadline without Well Defined Requirements',
            year='2019',
            rated='PG-13',
            released_on='2019-03-08',
            genre='Horror, Triller',
            director='William Palacios',
            plot='A huge project has arrived, clients services stablished a one-month timeline without defining proper requirements... What is the dev team going to do to deliver the software just-in-time??? D:',
            created_at='2019-08-20T00:00:00+03:00',
            updated_at='2019-08-20T00:00:00+03:00'
        )

    def test_index(self):
        resp = self.client.get('/movies/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['movie_list']), 1)

    def test_detail(self):
        resp = self.client.get('/movies/8/')
        self.assertEqual(resp.status_code, 200)

    def test_create(self):
        resp = self.client.get('/movies/create/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/movies/create/', {
            'title':'Testing in Production - The Movie',
            'year':'2019',
            'rated':'PG-13',
            'released_on':'2019-03-08',
            'genre':'Horror, Triller',
            'director':'William Palacios',
            'plot':'Even in 2019, after some years of software development evolution, some developers have adopted the horrible practice of testing in production...',
            'created_at':'2019-08-20T00:00:00+03:00',
            'updated_at':'2019-08-20T00:00:00+03:00'
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Testing in Production - The Movie')
        self.assertContains(resp, 'The movie created successfully')

    def test_create_field_required(self):
        resp = self.client.post('/movies/create/', {
            'title':'',
            'year':'2019',
            'rated':'PG-13',
            'released_on':'2019-03-08',
            'genre':'Horror, Triller',
            'director':'William Palacios',
            'plot':'Even in 2019, after some years of software development evolution, some developers have adopted the horrible practice of testing in production...',
            'created_at':'2019-08-20T00:00:00+03:00',
            'updated_at':'2019-08-20T00:00:00+03:00'
        }, follow=True)
        self.assertContains(resp, 'The creation has failed')
        self.assertFormError(resp, 'form', 'title',
                             'This field is required.')

    def test_create_err_title_exists(self):
        resp = self.client.post('/movies/create/', {
            'title':'Testing in Production - The Movie',
            'year':'2019',
            'rated':'PG-13',
            'released_on':'2019-03-08',
            'genre':'Horror, Triller',
            'director':'William Palacios',
            'plot':'Even in 2019, after some years of software development evolution, some developers have adopted the horrible practice of testing in production...',
            'created_at':'2019-08-20T00:00:00+03:00',
            'updated_at':'2019-08-20T00:00:00+03:00'
        }, follow=True)
        self.assertContains(resp, 'The creation has failed')
        self.assertFormError(resp, 'form', 'Title',
                             'Movie with this Title already exists.')

    def test_update(self):
        resp = self.client.get('/movies/update/8/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/movies/update/8/', {
            'title':'Tight Deadline without Well Defined Requirements',
            'year':'2019',
            'rated':'PG-13',
            'released_on':'2019-03-08',
            'genre':'Horror, Triller',
            'director':'Jose Matus',
            'plot':'Even in 2019, after some years of software development evolution, some developers have adopted the horrible practice of testing in production...',
            'created_at':'2019-08-20T00:00:00+03:00',
            'updated_at':'2019-08-20T00:00:00+03:00'
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Jose Matus')
        self.assertContains(resp, 'The movie updated successfully')

    def test_update_wrong_release_date(self):
        resp = self.client.post('/movies/update/8/', {
            'title':'Tight Deadline without Well Defined Requirements',
            'year':'2019',
            'rated':'PG-13',
            'released_on':'a_release_date',
            'genre':'Horror, Triller',
            'director':'Jose Matus',
            'plot':'Even in 2019, after some years of software development evolution, some developers have adopted the horrible practice of testing in production...',
            'created_at':'2019-08-20T00:00:00+03:00',
            'updated_at':'2019-08-20T00:00:00+03:00'
        }, follow=True)
        self.assertContains(resp, 'The update has failed')
        self.assertFormError(resp, 'form', 'released_on', 'Enter a valid date.')

    def test_delete(self):
        resp = self.client.get('/movies/delete/8/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/movies/delete/8/', follow=True)
        self.assertContains(resp, 'The movie deleted successfully')
