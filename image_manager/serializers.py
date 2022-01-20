
from rest_framework import serializers
from .models import Image, Description


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('__all__')

class DescriptionSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=200, allow_blank=True)

    class Meta:
        model = Description
        fields = ('__all__')
