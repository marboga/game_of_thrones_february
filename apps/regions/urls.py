from django.conf.urls import url

from . import views

app_name = "region"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^waffles$', views.create_region, name="create_region"),
]
