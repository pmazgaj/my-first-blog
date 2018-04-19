"""
Defines urls for API in application
"""

from django.conf.urls import url
from .views import ShopListApiView, ShopDetailApiView

urlpatterns = [
    url(r'^shop/?$', ShopListApiView.as_view()),
    url(r'^shop/(?P<id>[\w-]+)/$', ShopDetailApiView.as_view(), name='detail'),
]
