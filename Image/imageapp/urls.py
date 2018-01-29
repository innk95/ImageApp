from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'imageapp'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload/$', views.upload),
    url(r'^error/$', views.error),
    url(r'^(?P<image_id>[0-9]+)/$', views.detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)