from django.conf.urls import url
from webadmin import  views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webadmin'
urlpatterns = [
    url(r'^$', views.home),
    url(r'currency_detail$', views.currency_detail),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


