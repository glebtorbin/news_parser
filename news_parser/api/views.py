from rest_framework import viewsets
from rest_framework import filters

from news.models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('tags',)
    ordering_fields = ('pub_date',)
