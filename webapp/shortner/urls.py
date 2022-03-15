from django.urls import path

from webapp.ioc import get_ioc_view

from webapp.shortner.views import UrlAdder, UrlGetter

urlpatterns = [
    path('urls/', get_ioc_view(UrlAdder), name='add_url'),
    path('t/<str:token>', get_ioc_view(UrlGetter), name='get_url')
]
