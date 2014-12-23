from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from foo.banana.models import Banana
from foo.banana.views import BananaDetail, BananaRelatedDetail, BananaListView, BananaRelatedListView

urlpatterns = patterns('',
                       url(r'^$', BananaListView.as_view(model=Banana)),
                       url(r'^detail$', BananaListView.as_view(model=Banana)),
                       url(r'^related$', BananaRelatedListView.as_view(model=Banana)),
                       url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Banana)),
                       url(r'^(?P<pk>\d+)/detail$', BananaDetail.as_view()),
                       url(r'^(?P<pk>\d+)/related$', BananaRelatedDetail.as_view()))
