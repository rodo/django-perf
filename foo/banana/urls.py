from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from foo.banana.models import Apple
from foo.banana.views import AppleDetail, AppleRelatedDetail, AppleListView, AppleRelatedListView

urlpatterns = patterns('',
                       url(r'^$', AppleListView.as_view(model=Apple)),
                       url(r'^detail$', AppleListView.as_view(model=Apple)),
                       url(r'^related$', AppleRelatedListView.as_view(model=Apple)),
                       url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Apple)),
                       url(r'^(?P<pk>\d+)/detail$', AppleDetail.as_view()),
                       url(r'^(?P<pk>\d+)/related$', AppleRelatedDetail.as_view()))
