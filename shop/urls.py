"""
Defines urls for post applications (separately).
Home page - shop_list. Remnant - suburls.
"""

from django.conf.urls import include, url

from .views import (shop_list, shop_create, shop_edit, shop_delete, shop_detail)

urlpatterns = [
    url(r'^$', shop_list),
    url(r'^create/$', shop_create),
    url(r'^edit/$', shop_edit),
    url(r'^delete/$', shop_delete),
    url(r'^detail/$', shop_detail),

]
