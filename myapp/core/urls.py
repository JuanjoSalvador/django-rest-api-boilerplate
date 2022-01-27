from django.urls import path, re_path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter
from core.views import TestViewset

router = DefaultRouter()
router.register('test', TestViewset, basename='test-view'),

urlpatterns = router.urls
