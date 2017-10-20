# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PostsListView, PostsDetailView
__author__ = "spi4ka"


urlpatterns = [
    url(
        r'^$',
        PostsListView.as_view(),
        name="django-blogposts-list",
    ),

    url(
        r'^category/(?P<pk>\d+)/(?P<slug>[^\.]+)/$',
        PostsListView.as_view(),
        name="django-category-blogposts-list",
    ),

    url(
        r'^(?P<pk>\d+)/(?P<slug>[^\.]+)/$',
        PostsDetailView.as_view(),
        name="django-blogposts-detail",
    )
]
