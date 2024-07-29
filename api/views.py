from rest_framework import viewsets, permissions

from api.models import InteriorDesigner
from api.serializers import InteriorDesignerSerializer


class InteriorDesignerViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = InteriorDesigner.objects.all()
    serializer_class = InteriorDesignerSerializer
