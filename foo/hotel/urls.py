from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from foo.hotel.models import Hotel
from foo.hotel.views import HotelLimitListView
from foo.hotel.views import HotelLimitNoOrderListView

urlpatterns = patterns('',
                       url(r'^$', HotelLimitListView.as_view(model=Hotel), name='hotel'),
                       url(r'^noorder$', HotelLimitNoOrderListView.as_view(model=Hotel), name='hotelnoorder'))
