from django.conf.urls import url

from board.views import *

urlpatterns = [
    # Example: /
    url(r'^$', BostList.as_view(), name='index'),

    # Example: /board/?page=3
    # https://goo.gl/BRFiJV
    url(r'^postlist/page(?P<page>[0-9]+)/$', BostList.as_view(), name='post_list'),

    # # Example: /post/add/
    # url(r'^post/add/$', BostCreate.as_view(), name="post_add",),

    # Example: /post/99/
    url(r'^post/(?P<pk>\d+)/$', BostDetail.as_view(), name='post_detail'),

    # # Example: /post/99/update/
    # url(r'^post/(?P<pk>[0-9]+)/update/$', BostUpdate.as_view(), name="post_update",),

    # # Example: /post/99/delete/
    # url(r'^post/(?P<pk>[0-9]+)/delete/$', BostDelete.as_view(), name="post_delete",),
]