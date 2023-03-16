from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category
from ..category.serializers import CategorySerializer
from ..user.permissions import AdminPermission


class CategoryViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminPermission, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('category__slug',)
