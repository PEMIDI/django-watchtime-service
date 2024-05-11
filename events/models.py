from django.db import models
from django.db.models import Sum


class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

    def total_watch_time(self):
        total_watch_time = self.objects.all().annotate(total_watch_time=Sum('watch_time'))
        return total_watch_time


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class WatchTime(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="watch_time")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watch_time')
    total_watch_time = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f"{self.user} watched movie {self.movie} at {self.total_watch_time}"

    def update_watch_time(self, new_watch_time):
        self.total_watch_time += new_watch_time
        self.save()
        return self.total_watch_time

