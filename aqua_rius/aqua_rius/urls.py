from django.conf.urls import url, include
from rest_framework import routers
from app import apis

urlpatterns = [
    url(r'^api/', include(apis.router.urls)),
]
