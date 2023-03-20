from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Genre
from ..genre.serializers import GenreSerializer
from ..user.permissions import AdminUserOrReadOnly


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Класс представления обьектов модели Genre через
        одноимённый сериалайзер, используя Миксины на для запросов
        на удаление, создание и получение обьектов. Реализованы так же
        разрешение на доступ, поиск и пагинация обьектов"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminUserOrReadOnly, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
