from rest_framework.serializers import ModelSerializer

from reviews.models import Genre


class GenreSerializer(ModelSerializer):
    """Класс сериалайзера для всех запросов к
    обьектам модели Genre"""

    class Meta:
        model = Genre
        fields = ('name', 'slug')
