# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework_api_key.permissions import HasAPIKey


from .models import Movie
from .encoders import ExtendedEncoder
from .serializers import MovieSerializer


class MovieListView(APIView):
    """Show all movies."""
    permission_classes = [HasAPIKey]
    def get(self, request):
        queryset = Movie.objects.all()
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')


class MovieDetailView(APIView):
    """Show the requested movie."""
    permission_classes = [HasAPIKey]
    def get(self, request, isbn):
        query = Movie.objects.get(pk=isbn)
        return JsonResponse(query, encoder=ExtendedEncoder, safe=False)


class MovieCreateView(CreateAPIView):
    """Create a new movie."""
    serializer_class = MovieSerializer


class MovieUpdateView(UpdateView):
    """Update the requested movie."""


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
