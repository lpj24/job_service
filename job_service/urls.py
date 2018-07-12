"""job_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from jobs.views import JobViewSet, CategoryViewSet, ErrorJobViewSet
from jobs.tasks import execute_day_job
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()


router.register(r'api/jobs', JobViewSet, base_name='jobs')
router.register(r'api/categorys', CategoryViewSet)
router.register(r'api/errorJobs', ErrorJobViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/action/execute', execute_day_job),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
