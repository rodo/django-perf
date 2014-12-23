from django.views.generic import DetailView
from django.db.models import Count
from foo.dali.models import Fish


from django.views.generic import ListView

class FishListView(ListView):
    model = Fish
    paginate_by = 10

class FishListExistsView(ListView):
    model = Fish
    paginate_by = 10

    def get_queryset(self):
        fish = Fish.objects.annotate(num_fishon=Count('fishon'))
        return fish


class FishRelatedListView(ListView):
    model = Fish
    paginate_by = 10

    def get_queryset(self):
        fish = Fish.objects.all().select_related()
        return fish

class FishDetail(DetailView):
    model = Fish
    template_name = "fish/fish_detail.html"

class FishRelatedDetail(DetailView):
    model = Fish
    template_name = "fish/fish_detail.html"

    def get_object(self):
        fish = Fish.objects.filter(pk=self.kwargs['pk']).select_related()
        return fish[0]
                    

