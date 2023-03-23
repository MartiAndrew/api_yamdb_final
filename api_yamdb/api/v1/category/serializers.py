from rest_framework.serializers import ModelSerializer

from reviews.models import Category


class CategorySerializer(ModelSerializer):
    """Класс сериалайзера для всех запросов
    к обьектам модели Category"""

    class Meta:
        model = Category
        fields = ('name', 'slug')
