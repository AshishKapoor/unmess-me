from rest_framework import viewsets

from api.models import Movie
from api.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
