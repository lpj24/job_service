# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Job, Category, ErrorJob
from django.contrib import admin


class JobAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ErrorJobAdmin(admin.ModelAdmin):
    pass


from django.contrib import admin
from kombu.transport.django import models as kombu_models

admin.site.register(kombu_models.Message)

admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ErrorJob, ErrorJobAdmin)