from rest_framework import serializers
from .models import User, Pereval, Coord, ActivityType, Level, Image

class UserSerializer(serializers.ModelSerializer):
    fam = serializers.CharField(source="last_name")
    name = serializers.CharField(source="first_name")
    otc = serializers.CharField(source="patronymic")

    class Meta:
        model = User
        fields = ['fam', 'name', 'otc', 'email', 'phone']
        extra_kwargs = {
            'email': {'read_only': True},
            'last_name': {'read_only': True},
            'first_name': {'read_only': True},
            'patronymic': {'read_only': True},
            'phone': {'read_only': True},
        }

class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'spring', 'autumn']

class ImageSerializer(serializers.ModelSerializer):
    data = serializers.ImageField(source="image")

    class Meta:
        model = Image
        fields = ['title', 'data']

class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images', 'status']
        read_only_fields = ['status', 'add_time']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults={
                'last_name': user_data['last_name'],
                'first_name': user_data['first_name'],
                'patronymic': user_data.get('patronymic', ''),
                'phone': user_data['phone']
            }
        )

        pereval = Pereval.objects.create(user=user, **validated_data)

        Coord.objects.create(pereval=pereval, **coords_data)
        Level.objects.create(pereval=pereval, **level_data)

        for image_data in images_data:
            Image.objects.create(
                pereval=pereval,
                title=image_data.get('title', ''),
                image=image_data['image']
            )
        return pereval

    def update(self, instance, validated_data):
        coords_data = validated_data.pop('coords', None)
        if coords_data:
            coord = instance.coords
            for attr, value in coords_data.items():
                setattr(coord, attr, value)
            coord.save()

        level_data = validated_data.pop('level', None)
        if level_data:
            level = instance.level
            for attr, value in level_data.items():
                setattr(level, attr, value)
            level.save()

        images_data = validated_data.pop('images', None)
        if images_data:
            instance.images.all().delete()
            for image_data in images_data:
                Image.objects.create(
                    pereval=instance,
                    title=image_data.get('title', ''),
                    image=image_data['image']
                )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance