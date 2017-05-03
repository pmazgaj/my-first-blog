from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include("shop.urls", namespace='shop')),
    url(r'^api/', include("shop.api.urls")),


    # url(r'^api.auth/$', views.AuthView.as_view(), name="authenticate"),

    # url(r'^shops/$', include("<appname>.views.<function_name>")),
    # or from appname import views
    # url(r'^shops/$', views.<function_name(view_name)>)),
    # this does not work (don't know why)url(r'^shop/', "post.views.shop_home"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
