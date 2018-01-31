from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # create
    url(r'create$', views.create, name='create'),
    # delete
    # url(r'^/confirm$', views.confirm, name='confirm'),
    # url(r'^quote/(?P<id>\d+)/delete$', views.delete, name="delete"),
    # 
    url(r'^delete/(?P<quote_id>\d+)$', views.delete, name='delete'),
    # url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),

    # url(r'delete/$', views.delete, name='delete'),
    url(r'^(?P<quote_id>\d+)$', views.show, name='show'),
    url(r'^(?P<quote_id>\d+)/favorite$', views.favorite, name='favorite')
]