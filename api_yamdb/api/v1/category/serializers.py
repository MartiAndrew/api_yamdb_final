from rest_framework.serializers import ModelSerializer

from reviews.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')