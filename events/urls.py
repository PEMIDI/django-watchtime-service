from django.urls import path

from events import views

"""
URL patterns for events API 📈
"""

urlpatterns = [
    # URL pattern for retrieving the list of events
    path('', views.EventAPI.as_view(), name='event-list'),

    # URL pattern for retrieving the total watch time of a user 👥
    path('users/<str:username>/total-watch-time/', views.UserTotalWatchTimeAPI.as_view(), name='user-watch-time'),

    # URL pattern for retrieving the total watch time of a movie 🎥
    path('movies/<int:pk>/total-watch-time/', views.MovieTotalWatchTimeAPI.as_view(), name='movie-watch-time')
]
