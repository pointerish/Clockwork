# -*- coding: utf-8 -*-

"""Movies views."""

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
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
    def get(self, request, pk):
        query = Movie.objects.get(pk=pk)
        return JsonResponse(query, encoder=ExtendedEncoder, safe=False)


class MovieCreateView(CreateAPIView):
    """Create a new movie."""
    permission_classes = [HasAPIKey]
    serializer_class = MovieSerializer


class MovieUpdateView(UpdateAPIView):
    """Update the requested movie."""
    permission_classes = [HasAPIKey]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDeleteView(DestroyAPIView):
    """Delete the requested movie."""
    permission_classes = [HasAPIKey]
    queryset = Movie.objects.all()
