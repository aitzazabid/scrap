from django.conf.urls import url
from webadmin import  views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webadmin'
urlpatterns = [
    url(r'^$', views.home),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


