# Create your views here.
# Sigafo map views
#
#
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView
from django.contrib.gis.shortcuts import render_to_kml
from django.http import HttpResponse
from foo.july.models import Book, Author, Editor
from faker import Faker
from random import randrange
from django.shortcuts import render
from django.views.generic.detail import DetailView


class BookDetail(DetailView):
    template_name = 'july/book_detail.html'

class BookDetailUsing(DetailView):
    template_name = 'july/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailUsing, self).get_context_data(**kwargs)
        context['nb_editors'] = Editor.objects.using('readonly').count()
        return context


def create_book(request):
    """
    Retrieve, update or delete a code map.
    """
    f = Faker()

    nbpage = randrange(10)

    Author.objects.create(last_name=f.last_name()[:30],
                          first_name=f.first_name()[:30])
    
    editor = Editor(name=f.last_name()[:30])

    author = Author.objects.all().last()
    
    book = Book.objects.create(author=author,
                               title=" ".join(f.words())[:30],
                               nbpages=nbpage)

    nb = Book.objects.filter(nbpages=nbpage).count()

    return render(request, 'july/book_create.html', {"count": nb},
                  content_type="text/html")
