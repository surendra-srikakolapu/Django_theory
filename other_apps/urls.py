from django.conf import settings
from django.urls import path, re_path

from other_apps.views import Files
from django.views.static import serve
from .views import *


urlpatterns = [

    path('file', Files, name='download-list'),
    re_path
    (r'download/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    path('portfolio', Portfolio, name='portfolio'),

]
