from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from home.forms import AddressForm
from home.models.person import Person

from .models.address import Address


class HomeView(TemplateView):
    template_name = "hello_world.html"


class PeopleView(ListView):
    paginate_by = 10
    model = Person

    def post(self, q: str, *args, **kwargs):
        return render("hello_world.html")

    def get_queryset(self):
        query_set = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            query_set = query_set.filter(first_name=query)

        return query_set


class PersonDetailView(DetailView):
    model = Person


class AddressListView(ListView):
    paginate_by = 20
    model = Address


class AddressDetailView(DetailView):
    model = Address


class AddressCreateView(CreateView):
    model = Address
    fields = ['street', 'unit_number', 'city', 'province', 'postal_code', 'country']


class AddressUpdateView(UpdateView):
    model = Address
    fields = ['street', 'unit_number', 'city', 'province', 'postal_code', 'country']


class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy("address_list")


class AddressView(FormView):
    template_name = "address_form.html"
    form_class = AddressForm
    success_url = ""

    def form_valid(self, form: AddressForm):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.instance.save()
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):

    #     context = {
    #         "form": AddressForm()
    #     }

    #     return render(request, "address_form.html", context)

    # def post(self, request, *args, **kwargs):

    #     address = AddressForm(data=request.POST)
    #     if address.is_valid():
    #         address.instance.save()

    #     context = {
    #         "form": address
    #     }

    #     return render(request, "address_form.html", context)
