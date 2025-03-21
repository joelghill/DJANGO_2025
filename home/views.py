from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from home.models.person import Person


class HomeView(View):
    def get(self, request):
        context = {"username": "guy"}

        return render(request, "hello_world.html", context=context)


def list_people_view(request: HttpRequest) -> HttpResponse:
    silly_things = {"people": Person.objects.filter(first_name="Billy")}

    return render(request, "people_view.html", context=silly_things)
