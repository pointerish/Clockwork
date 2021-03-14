from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = 'moviesapp.movies'
    verbose_name = 'Movies'

    def ready(self):
        pass
