from rest_framework.serializers import ModelSerializer
from .models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "year", "rated",
                  "released_on", "genre", "director",
                  "plot")
