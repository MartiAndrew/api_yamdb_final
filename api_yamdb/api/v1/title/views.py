from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination

from .models import Title
from .serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'year', 'genre__slug', 'category__slug')