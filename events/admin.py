from django.contrib import admin
from .models import CustomUser, Movie, WatchTime


class WatchTimeInline(admin.TabularInline):
    model = WatchTime
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [WatchTimeInline]


admin.site.register(Movie, MovieAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(CustomUser, CustomUserAdmin)
