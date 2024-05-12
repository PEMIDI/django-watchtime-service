from django.db import models, transaction
from django.db.models import Sum


class CustomUser(models.Model):
    """Custom user model 👨‍💻"""
    username = models.CharField(max_length=100, unique=True)  # 👤

    def __str__(self):
        """Return the username as a string"""
        return self.username

    @property
    def total_watch_time(self):
        """Get the total watch time for this user ⏰"""
        total_watch_time = self.watch_time.aggregate(Sum('total'))['total__sum']
        return total_watch_time


class Movie(models.Model):
    """Movie model 🎥"""
    title = models.CharField(max_length=100, blank=True, null=True)  # 📽
    slug = models.SlugField(unique=True)  # 🔗

    def __str__(self):
        """Return the movie slug as a string"""
        return self.slug

    @property
    def total_watch_time(self):
        """Get the total watch time for this movie ⏰"""
        total_watch_time = self.watch_time.aggregate(Sum('total'))['total__sum']
        return total_watch_time


class WatchTime(models.Model):
    """Watch time model ⏱️"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="watch_time")  # 👥
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watch_time')  # 🎬
    last_moment = models.PositiveIntegerField(default=0)  # ⏱️
    total = models.PositiveIntegerField(default=0)  # 📊

    def __str__(self):
        """Return a string representation of the watch time"""
        return f"{self.user} watched movie {self.movie} at {self.total}"

    def update_watch_time(self, new_watch_time):
        """Update the watch time for this instance ⏱️"""
        self.total += new_watch_time
        if new_watch_time > self.last_moment:
            self.last_moment = new_watch_time
        self.save()
        return self.total

    @classmethod
    def save_watch_time_from_broker(cls, data):
        """
        Save watch time from broker data 💻

        Args:
            data (dict): Broker data containing user, movie, and watch time

        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            with transaction.atomic():
                username = data.get('user')
                movie_slug = data.get('slug')
                new_watch_time = data.get('at')

                user, created = CustomUser.objects.get_or_create(username=username)
                movie, created = Movie.objects.get_or_create(slug=movie_slug)

                watch_time, status = WatchTime.objects.update_or_create(user=user, movie=movie)

                watch_time.update_watch_time(new_watch_time)
                watch_time.save()
            return True
        except (Exception,):
            return False
