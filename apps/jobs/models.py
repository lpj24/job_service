# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """
        任务所属类别
    """
    CATEGORY_TYPE_CODE = (
        (1, "航班"),
        (2, "高铁"),
        (3, "活力"),
        (4, "localytics"),
    )
    id = models.IntegerField(choices=CATEGORY_TYPE_CODE, primary_key=True, blank=False, unique=True, verbose_name='类别代码')
    create_time = models.DateTimeField(auto_now=True, verbose_name="添加时间", editable=False)
    class Meta:
        verbose_name = '模块大类'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __unicode__(self):
        return self.get_id_display()


# BI任务模型
class Job(models.Model):

    JOB_TYPE_CODE = (
        (1, '每天更新的任务'),
        (2, '每周更新的任务'),
        (3, '每月更新的任务'),
        (4, '每季度更新'),
        (5, '发送邮件'),
    )
    job_name = models.CharField(max_length=100, verbose_name='任务函数')
    job_path = models.CharField(max_length=200, verbose_name='任务路径')
    job_doc = models.CharField(max_length=500, verbose_name='任务描述')
    job_table = models.CharField(max_length=100, verbose_name='操作表名')
    category_type = models.ForeignKey(Category, verbose_name='任务所属类别', related_name='job_nodes')
    # category可以同job_nodes反向查找其类别下所有的列表
    job_type = models.IntegerField(choices=JOB_TYPE_CODE, verbose_name='任务所属类型')
    is_execute = models.BooleanField(verbose_name='能否直接执行', default=1)
    create_time = models.DateTimeField(auto_now=True, verbose_name="添加时间", editable=False)
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间", editable=False)

    class Meta:
        db_table = 'bi_execute_job'
        verbose_name = '任务'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
        unique_together = ['job_name', 'job_table']

    def __unicode__(self):
        return self.job_name


class ErrorJob(models.Model):
    s_day = models.CharField(max_length=50, verbose_name=u'日期')
    error_job = models.OneToOneField(Job)

    class Meta:
        db_table = 'error_update_table_daily'
        verbose_name = '未更新成功的任务'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.error_job.job_name
