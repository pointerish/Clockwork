# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from .models import Movie
from .encoders import ExtendedEncoder


class MovieListView(ListView):
    """Show all movies."""
    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')


class MovieDetailView(DetailView):
    """Show the requested movie."""
    def get(self, request, isbn, *args, **kwargs):
        query = Movie.objects.get(pk=isbn)
        return JsonResponse(query, encoder=ExtendedEncoder, safe=False)


class MovieCreateView(CreateView):
    """Create a new movie."""


class MovieUpdateView(UpdateView):
    """Update the requested movie."""


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""