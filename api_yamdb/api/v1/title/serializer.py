from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Comment, Review, Category, Title, Genre

class TitleSerializer(ModelSerializer):
    category = SlugRelatedField(queryset=Category.objects.all(),
                                slug_field='slug')
    genre = SlugRelatedField(queryset=Genre.objects.all(),
                             slug_field='slug')
    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category')
        model = Title