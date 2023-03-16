from rest_framework.serializers import ModelSerializer

from reviews.models import Genre


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')