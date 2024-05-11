from django.db import models
from django.db.models import Sum


class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

    @property
    def total_watch_time(self):
        total_watch_time = self.watch_time.aggregate(Sum('total'))['total__sum']
        return total_watch_time


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    @property
    def total_watch_time(self):
        total_watch_time = self.watch_time.aggregate(Sum('total'))['total__sum']
        return total_watch_time


class WatchTime(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="watch_time")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watch_time')
    last_moment = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} watched movie {self.movie} at {self.total}"

    def update_watch_time(self, new_watch_time):
        self.total += new_watch_time
        if new_watch_time > self.last_moment:
            self.last_moment = new_watch_time
        self.save()
        return self.total
