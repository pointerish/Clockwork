from django.contrib import admin

from .models import Movie, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    pass
