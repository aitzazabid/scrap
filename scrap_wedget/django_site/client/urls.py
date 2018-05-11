from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from client.api import *

urlpatterns = [
    url('^coincap', coincap),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



