from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            'email',
            'phone',
            'name',
            'surname',
            'patronymic',
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height'
        ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring'
        ]


class ImagesSerializer(serializers.ModelSerializer):
    images = serializers.URLField()

    class Meta:
        model = Images
        fields = [
            'name',
            'images',
        ]


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    user = AppUserSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = [
            'id',
            'status',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'coord_id',
            'user',
            'level',
            'images',
        ]
