from django.conf.urls import include, url
from django.contrib import admin

# from shop import views as post_view
# from shop import views as post_view


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include("shop.urls")),

    # url(r'^shops/$', include("<appname>.views.<function_name>")),
    # or from appname import views
    # url(r'^shops/$', views.<function_name(view_name)>)),
    # this does not work (don't know why)url(r'^shop/', "post.views.shop_home"),
]

