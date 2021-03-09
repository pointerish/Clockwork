from django.contrib import admin

from .models import Movie, User, Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
