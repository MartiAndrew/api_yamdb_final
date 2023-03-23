from django_filters import rest_framework as filters

from reviews.models import Title


class TitleFilter(filters.FilterSet):
    """Класс-фильтр для модели Title для полей фильтрации,
    описанных в Meta-классе с атрибутами"""
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='icontains'
    )
    genre = filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = '__all__'
