from rest_framework import serializers

from api.models import InteriorDesigner


class InteriorDesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorDesigner
        fields = '__all__'

