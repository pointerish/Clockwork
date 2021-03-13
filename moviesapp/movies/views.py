# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework_api_key.permissions import HasAPIKey
import django_filters.rest_framework

from .models import Movie, Review
from .encoders import ExtendedEncoder
from .serializers import MovieSerializer, ReviewSerializer, MovieSearchSerializer


class MovieListView(APIView):
    """Show all movies."""

    def get(self, request):
        queryset = Movie.objects.order_by('-created_at', 'reviews')
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')


class MovieDetailView(APIView):
    """Show the requested movie."""
    # permission_classes = [HasAPIKey]

    def get(self, request, pk):
        query = Movie.objects.get(pk=pk)
        return JsonResponse(query, encoder=ExtendedEncoder, safe=False)


class MovieCreateView(CreateAPIView):
    """Create a new movie."""
    # permission_classes = [HasAPIKey]

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Feed me movie data, please.'}, safe=False, status=200)

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': f'{request.data["title"]} - The movie created successfully'},
                                 safe=False, status=200)
        return JsonResponse({'message': 'The creation has failed', 'form': serializer.errors}, safe=False, status=400)


class MovieUpdateView(UpdateAPIView, UpdateModelMixin):
    """Update the requested movie."""
    # permission_classes = [HasAPIKey]

    def put(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'The movie updated successfully', 'form': {request.data}}, safe=False, status=200)
        return JsonResponse({'message': 'The update has failed', 'form': serializer.errors}, safe=False, status=400)

    def post(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDeleteView(DestroyAPIView):
    """Delete the requested movie."""
    permission_classes = [HasAPIKey]
    queryset = Movie.objects.all()


class ReviewListView(APIView):
    """Show all reviews."""
    # permission_classes = [HasAPIKey]

    def get(self, request):
        queryset = Review.objects.all()
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')


class ReviewDetailView(APIView):
    """Show the requested review."""
    permission_classes = [HasAPIKey]

    def get(self, request, pk):
        query = Review.objects.get(pk=pk)
        return JsonResponse(query, encoder=ExtendedEncoder, safe=False)


class ReviewCreateView(CreateAPIView):
    """Create a new review."""
    # permission_classes = [HasAPIKey]
    serializer_class = ReviewSerializer


class ReviewUpdateView(UpdateAPIView):
    """Update the requested review."""
    permission_classes = [HasAPIKey]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDeleteView(DestroyAPIView):
    """Delete the requested review."""
    permission_classes = [HasAPIKey]
    queryset = Review.objects.all()


class MovieSearchView(ListAPIView):

    # permission_classes = [HasAPIKey]

    queryset = Movie.objects.all()
    serializer_class = MovieSearchSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ("title", "year", "rated",
                     "released_on", "genre", "director",)
