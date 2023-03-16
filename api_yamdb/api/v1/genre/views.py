from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Genre
from ..genre.serializers import GenreSerializer
from ..user.permissions import AdminPermission


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminPermission, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('genre__slug',)
