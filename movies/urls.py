from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.MoviesView.as_view()),
    path("movies/<int:movie_id>/", views.MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", views.MovieOrderView.as_view()),
]
