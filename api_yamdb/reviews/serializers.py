from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Comment, Review, Category, Title

class TitleSerializer(ModelSerializer):
    category = SlugRelatedField(queryset=Category.objects.all(),
                                slug_field='slug')
    genre = SlugRelatedField(queryset=Genre.objects.all(),
                             slug_field='slug')
    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category')
        model = Title


class ReviewSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        read_only_fields = ('review',)
        model = Comment
