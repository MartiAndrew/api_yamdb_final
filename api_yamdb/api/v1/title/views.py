import django_filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Title
from ..title.serializers import TitleSerializer
from ..user.permissions import AdminPermission


class TitleFilter(django_filters.FilterSet):
    class Meta:
        model = Title
        fields = {'name':['iexact','icontains'],
                  'year':['lte','gte'],
                  'genre__slug':['iexact','icontains'],
                  'category__slug':['iexact','icontains']
                  }

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminPermission,)
    filterset_fields = TitleFilter
