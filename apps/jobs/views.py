# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, mixins
from .models import Job, Category, ErrorJob
from rest_framework import filters
from .serializers import JobSerializers, CategorySerializer, ErrorJobSerializers
import datetime
import logging
from rest_framework_extensions.cache.mixins import CacheResponseMixin


class CategoryViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer


class JobViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    filter_backends = (filters.SearchFilter, )
    search_fields = ('job_table', 'job_doc')


class ErrorJobViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = ErrorJob.objects.select_related("error_job").all()

    def get_queryset(self):
        return self.queryset.filter(s_day=str(datetime.date.today() - datetime.timedelta(days=1)))
    serializer_class = ErrorJobSerializers
