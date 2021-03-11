from rest_framework import serializers

from .models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "year", "rated",
                  "released_on", "genre", "director",
                  "plot")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("body", "stars", "movie")


class MovieSearchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    rated = serializers.CharField(max_length=64)
    released_on = serializers.DateField()
    genre = serializers.CharField(max_length=255)
    director = serializers.CharField(max_length=255)
    plot = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
