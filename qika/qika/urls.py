"""qika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
import re
from . import settings
from apps.anime.views import index
from apps.account.views import page_not_found

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('apps.users.urls', namespace='users')),
    url(r'^account/', include('apps.account.urls', namespace="account")),
    url(r'^apis/', include('apps.apis.urls', namespace="apis")),
    url(r'^tags/', include('apps.tags.urls', namespace="tags")),
    url(r'^anime/', include('apps.anime.urls', namespace='anime')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, {"document_root": settings.STATIC_ROOT}),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, {"document_root": settings.MEDIA_ROOT}),

]
handler404 = page_not_found
handler500 = page_not_found