from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^users/(?P<user_id>\d+)/index$', views.index),
    # url(r'^users/(?P<user_id>\d+)$', views.index),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^$', views.index),
    url(r'^create_house$', views.create_house, name='create_house'),
]
