from django.conf.urls import patterns, url

from organization import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index')
)
