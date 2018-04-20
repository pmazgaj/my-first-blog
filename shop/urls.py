"""
Defines urls for shop applications (separately).
Home page - shop_list. 
Remnant - suburls.
"""

from django.conf.urls import include, url

from shop.api import ShopListApiView
from .views import (shop_list, shop_create, shop_edit, shop_delete, shop_detail)

urlpatterns = [
    url(r'^$', ShopListApiView.as_view(), name='list'),
    url(r'^create/$', shop_create),
    url(r'^(?P<id>\d+)/edit/$', shop_edit, name='update'),
    url(r'^(?P<id>\d+)/delete/$', shop_delete),
    url(r'^(?P<id>\d+)/$', shop_detail, name='detail'),

]
