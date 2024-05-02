from rest_framework import viewsets

from api.models import Movie, TVShow
from api.serializers import MovieSerializer, TVShowSerializer


class MovieViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TVShowViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
