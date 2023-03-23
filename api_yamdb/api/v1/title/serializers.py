from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from reviews.models import Category, Genre, Review, Title

from ..category.serializers import CategorySerializer
from ..genre.serializers import GenreSerializer


class TitleSerializer(ModelSerializer):
    """Класс сериалайзера для всех запросов к обьектам модели Title"""
    category = SlugRelatedField(queryset=Category.objects.all(),
                                slug_field='slug'
                                )
    genre = SlugRelatedField(queryset=Genre.objects.all(),
                             many=True,
                             slug_field='slug'
                             )

    class Meta:
        fields = '__all__'
        model = Title


class TitleReadSerializer(ModelSerializer):
    """Класс сериалайзер для безопасных запросов
    к обьектам модели Title"""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True, )
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        reviews = Review.objects.filter(title=obj)
        if reviews:
            ratings_sum = sum(review.score for review in reviews)
            return round(ratings_sum / len(reviews))
        return None
