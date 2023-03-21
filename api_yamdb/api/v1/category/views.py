from rest_framework import viewsets, filters, mixins

from reviews.models import Category
from ..category.serializers import CategorySerializer
from ..user.permissions import AdminUserOrReadOnly


class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """Класс представления обьектов модели Category через
    одноимённый сериалайзер, используя Миксины на для запросов
    на удаление, создание и получение обьектов. Реализованы так же
    разрешение на доступ, поиск и пагинация обьектов"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminUserOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)
    lookup_field = 'slug'
