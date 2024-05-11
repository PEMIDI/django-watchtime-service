from django.urls import path

from events import views

urlpatterns = [
    path('', views.EventAPI.as_view(), name='event-list'),
    path('users/<str:username>/total-watch-time/', views.UserTotalWatchTimeAPI.as_view(), name='user-watch-time'),
    path('movies/<int:pk>/total-watch-time/', views.MovieTotalWatchTimeAPI.as_view(), name='movie-watch-time')
]
