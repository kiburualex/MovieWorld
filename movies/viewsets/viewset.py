from rest_framework import generics
from django.db.models import Q
from rest_framework import pagination
from rest_framework.response import Response

from movies.pagination.pgn import PgLimitOffsetPagination
from movies.models import Movie as Table
from movies.serializers.movies_serializer import (
    CreateSerializer,
    ListSerializer,
    UpdateSerializer
    )


import structlog
logger = structlog.get_logger('django_structlog')

class CreateAPIView(generics.CreateAPIView):
    serializer_class = CreateSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(generics.ListAPIView):
    serializer_class = ListSerializer
    pagination_class = PgLimitOffsetPagination

    """Add new key to context"""
    def get_serializer_context(self):
        date = self.request.GET.get('date')
        if date:
            return {"date": date, 'request': self.request}
        return {"date": None, 'request': self.request}

    def get_queryset(self, *args, **kwargs):
        display_size = self.request.GET.get('display_size')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        query = self.request.GET.get('query')
        
        queryset_list = Table.objects.all()

        if display_size:
            pagination.PageNumberPagination.page_size = display_size
        else:
            pagination.PageNumberPagination.page_size = 10

        if date_from and date_to:
            queryset_list = queryset_list.filter(created_at__range=(date_from, date_to))

        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query))
        
        logger.info("logging query results", count=queryset_list.count())
        return queryset_list.order_by('-id')


class UpdateAPIView(generics.UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = UpdateSerializer

    def get_serializer_context(self):
        return { 'request': self.request }

    def perform_update(self, serializer):
        try:
            instance = serializer.save()
            update_info = f"Update Poll id={instance.id} details [{instance}]"
        except Exception as e:
            logger.error('Error in Trail', error=e)


class RetrieveAPIView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = UpdateSerializer

    def get_serializer_context(self):
        return { 'request': self.request }

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)


class DestroyAPIView(generics.DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = UpdateSerializer

    def perform_destroy(self, instance):
        instance.delete()





