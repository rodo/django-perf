from django.shortcuts import render
from django.views.generic.detail import DetailView
from foo.july.models import Editor


class BookDetail(DetailView):
    template_name = 'bear/book_detail.html'

class BookDetailOpt(DetailView):
    template_name = 'bear/book_detail_opt.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailOpt, self).get_context_data(**kwargs)
        #context['editors'] = Editor.objects.filter(book_set__in=self.get_queryset())
        #print self.get_queryset()
        return context
