from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class WatchTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    total_watch_time = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f"{self.user} watched movie {self.movie} at {self.total_watch_time}"
