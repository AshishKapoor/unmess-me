from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.viewsets import ViewSetMixin

from api.models import Movie
from api.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
