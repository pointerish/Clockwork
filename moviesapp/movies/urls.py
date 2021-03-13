# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', view=views.MovieListView.as_view(), name='index'),
    path('<int:pk>/',
         view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:pk>/',
         view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',
         view=views.MovieDeleteView.as_view(), name='delete'),
    path('reviews/', view=views.ReviewListView.as_view(), name='review-index'),
    path('reviews/<int:pk>/',
         view=views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/create/', view=views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/update/<int:pk>/',
         view=views.ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/delete/<int:pk>/',
         view=views.ReviewDeleteView.as_view(), name='review-delete'),
    path('search/',
         view=views.MovieSearchView.as_view(), name='search'),
]
