from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from foo.dali.models import Fish
from foo.dali.views import FishDetail, FishRelatedDetail, FishListExistsView, FishListView, FishRelatedListView

urlpatterns = patterns('',
                       url(r'^exists$', FishListExistsView.as_view(template_name = "dali/fish_list_exists.html"), name="dali_exists"),
                       url(r'^$', FishListView.as_view(model=Fish), name="dali"),
                       url(r'^related$', FishRelatedListView.as_view(model=Fish)),
                       url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Fish)),
                       url(r'^(?P<pk>\d+)/detail$', FishDetail.as_view()),
                       url(r'^(?P<pk>\d+)/related$', FishRelatedDetail.as_view()))
