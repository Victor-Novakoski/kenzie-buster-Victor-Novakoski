from django.db import models


# Create your models here.
class Rating(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R_R = "R"
    NC_17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    synopsis = models.TextField(null=True)
    rating = models.CharField(
        max_length=20, choices=Rating.choices, default=Rating.DEFAULT
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )

    movie_users = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="movie_user",
    )

    def __repr__(self) -> str:
        return f"<Movie ({self.id}) - {self.tittle}>"


class MovieOrder(models.Model):
    movies = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_user",
    )

    users = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie",
    )

    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __repr__(self) -> str:
        return f"<MovieOrder [{self.id}] - {self.users}>"
