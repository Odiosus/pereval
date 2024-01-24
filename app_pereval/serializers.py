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

    def save(self, **kwargs):
        self.is_valid()
        user = AppUser.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = AppUser.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                name=self.validated_data.get('name'),
                surname=self.validated_data.get('surname'),
                patronymic=self.validated_data.get('otc'),
            )
            return new_user


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


class PerevalSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    user = AppUserSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)
    id = serializers.HyperlinkedIdentityField(view_name='pereval-detail')

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
        read_only_fields = ['status']
