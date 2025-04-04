from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from home.models.person import Person


class HomeView(TemplateView):
    template_name = "hello_world.html"


class PeopleView(ListView):
    paginate_by = 10
    model = Person


    def get_queryset(self):
        query_set = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            query_set = query_set.filter(first_name=query)
        
        return query_set


class PersonDetailView(DetailView):
    model = Person
