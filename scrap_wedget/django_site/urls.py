from django.conf.urls import  include, url
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import admin
from django.http import JsonResponse

#imgae upload setting
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^client/', include('client.urls')),
    url(r'^', include('webadmin.urls')),

]
