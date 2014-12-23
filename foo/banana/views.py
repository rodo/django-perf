
from django.views.generic import DetailView

from foo.banana.models import Banana


from django.views.generic import ListView

class BananaListView(ListView):
    model = Banana
    paginate_by = 10

class BananaRelatedListView(ListView):
    model = Banana
    paginate_by = 10

    def get_queryset(self):
        banana = Banana.objects.all().select_related()
        return banana


class BananaDetail(DetailView):
    model = Banana
    template_name = "banana/banana_detail.html"

class BananaRelatedDetail(DetailView):
    model = Banana
    template_name = "banana/banana_detail.html"

    def get_object(self):
        banana = Banana.objects.filter(pk=self.kwargs['pk']).select_related()
        return banana[0]
                    

