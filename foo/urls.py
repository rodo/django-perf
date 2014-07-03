from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView


from foo.bar.views import ClientDetail, ClientIdxDetail, ClientPrepDetail
from foo.bar.models import Client
from foo.july.models import Book

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Client)),
                       url(r'^noindex/(?P<pk>\d+)$', ClientDetail.as_view()),
                       url(r'^index/(?P<pk>\d+)$', ClientIdxDetail.as_view()),
                       url(r'^prepared/(?P<pk>\d+)$', ClientPrepDetail.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^book/(?P<pk>\d+)$', DetailView.as_view(model=Book, template_name='default_detail.html')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

