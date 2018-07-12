# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Job, Category, ErrorJob
from django.forms.fields import *


# api返回数据展示
class JobSerializers(serializers.ModelSerializer):

    job_name = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'

    def get_job_name(self, obj):
        return obj.job_name


class CategorySerializer(serializers.ModelSerializer):
    job_nodes = JobSerializers(many=True)
    category_name = serializers.CharField(source='get_id_display')
    class Meta:
        model = Category
        fields = '__all__'


class ErrorJobSerializers(serializers.ModelSerializer):
    error_job = JobSerializers()

    class Meta:
        model = ErrorJob
        fields = ('error_job',)


