from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Title
from ..title.serializers import TitleSerializer, TitleReadSerializer
from ..user.permissions import AdminUserOrReadOnly
from .filters import TitleFilter


class TitleViewSet(viewsets.ModelViewSet):
    """Класс вьюсет для работы с обьектами модели Title и их
    представления через Serializer. В нем предусмотрены разрешения,
    фильтрация и пагинация. А также предусмотрен выбор сериалазера
     в зависимости от типа запроса."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminUserOrReadOnly,)
    filterset_class = TitleFilter
    filter_backends = (DjangoFilterBackend,)
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleSerializer
