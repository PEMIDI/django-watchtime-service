from django.urls import path

from events import views

urlpatterns = [
    path('', views.EventAPI.as_view(), name='event-list'),
]
