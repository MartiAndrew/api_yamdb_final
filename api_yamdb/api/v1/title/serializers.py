from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers

from reviews.models import Category, Title, Genre

class TitleSerializer(ModelSerializer):
    category = SlugRelatedField(queryset=Category.objects.all(),
                                slug_field='slug')
    genre = SlugRelatedField(queryset=Genre.objects.all(),
                             many=True,
                             slug_field='slug')
    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category')
        model = Title

class TitleReadSerializer(ModelSerializer):
    category = SlugRelatedField(read_only=True,
                                slug_field='slug'
                                )
    genre = SlugRelatedField(many=True,
                             read_only=True,
                             slug_field='slug'
                             )
    rating = serializers.IntegerField()
    class Meta:
        fields = ('name', 'year', 'description', 'rating', 'genre', 'category')
        model = Title



