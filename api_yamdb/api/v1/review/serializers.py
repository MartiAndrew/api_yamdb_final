from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username'
                                          )
    title = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        user = self.context['request'].user
        title = self.context.get('view').kwargs.get('title_id')
        if (Review.objects.filter(title=title, author=user).exists()
                and self.context.get('request').method == 'POST'):
            raise serializers.ValidationError(
                'Вы уже оставили отзыв на это произведение!'
            )
        return data
