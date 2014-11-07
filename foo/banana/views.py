
from django.views.generic import DetailView

from foo.banana.models import Apple


from django.views.generic import ListView

class AppleListView(ListView):
    model = Apple
    paginate_by = 10

class AppleRelatedListView(ListView):
    model = Apple
    paginate_by = 10

    def get_queryset(self):
        apple = Apple.objects.all().select_related()
        return apple


class AppleDetail(DetailView):
    model = Apple
    template_name = "banana/apple_detail.html"

class AppleRelatedDetail(DetailView):
    model = Apple
    template_name = "banana/apple_detail.html"

    def get_object(self):
        apple = Apple.objects.filter(pk=self.kwargs['pk']).select_related()
        return apple[0]
                    

