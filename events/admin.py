from django.contrib import admin
from .models import CustomUser, Movie, WatchTime


class WatchTimeInline(admin.TabularInline):
    model = WatchTime
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [WatchTimeInline]

    list_display = ['id', 'title', 'slug', 'total_watch_time']


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'total_watch_time']


class WatchTimeAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'total']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(WatchTime, WatchTimeAdmin)
