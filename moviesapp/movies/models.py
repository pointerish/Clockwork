# -*- coding: utf-8 -*-
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self) -> str:
        return reverse('movies:detail', kwargs={'id': self.pk})


class Review(models.Model):

    ordering = ['-stars']

    body = models.TextField(blank=False, null=False)
    stars = models.PositiveIntegerField()
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f'{self.stars}'
