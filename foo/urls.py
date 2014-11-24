from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from foo.bar.views import ClientDetail, ClientIdxDetail, ClientPrepDetail
from foo.bar.models import Client
from foo.july.models import Book
from foo.july import views as julyviews
from foo.bear import views as bearviews


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name="home.html")),
                       url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Client)),
                       url(r'^noindex/(?P<pk>\d+)$', ClientDetail.as_view()),
                       url(r'^index/(?P<pk>\d+)$', ClientIdxDetail.as_view()),
                       url(r'^prepared/(?P<pk>\d+)$', ClientPrepDetail.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^book/(?P<pk>\d+)$', DetailView.as_view(model=Book, template_name='default_detail.html')),
                       url(r'^july/book/(?P<pk>\d+)$', julyviews.BookDetailUsing.as_view(model=Book), name='book_detail'),
                       url(r'^july/book/$', ListView.as_view(model=Book, template_name='july/book_list.html',
                                                             paginate_by=10), name='july_books'),
                       url(r'^july/book/create$', 'foo.july.views.create_book', name='july_book_create'),

                       url(r'^bear/book/(?P<pk>\d+)$', bearviews.BookDetail.as_view(model=Book), name='bear_book'),
                       url(r'^bear/book/(?P<pk>\d+)/opt$', bearviews.BookDetailOpt.as_view(model=Book), name='bear_book_opt'),

                       url(r'^bear/book/$', ListView.as_view(model=Book,
                                                             template_name='bear/book_list.html',
                                                             paginate_by=10), name='bear_books'),
                       
                       url(r'^banana/', include('foo.banana.urls'))
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

