"""
Defines urls for shop applications (separately).
Home page - shop_list. 
Remnant - suburls.
"""

from django.conf.urls import include, url

from .views import (shop_list, shop_create, shop_edit, shop_delete, shop_detail)

pattern_main_shop_list = url(r'^$', shop_list, name='list')
print(shop_list)

urlpatterns = [
    pattern_main_shop_list,
    url(r'^create/$', shop_create),
    url(r'^(?P<id>\d+)/edit/$', shop_edit, name='update'),
    url(r'^(?P<id>\d+)/delete/$', shop_delete),
    url(r'^(?P<id>\d+)/$', shop_detail, name='detail'),

]
