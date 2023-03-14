from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Comment, Review


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
