from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view() , name='list-create-movies'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view() , name='update-movies'),
]