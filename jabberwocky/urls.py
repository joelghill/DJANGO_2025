"""
URL configuration for jabberwocky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from home.views import (
    AddressCreateView,
    AddressDeleteView,
    AddressDetailView,
    AddressListView,
    AddressUpdateView,
    HomeView,
    PeopleView,
    PersonDetailView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("people/", PeopleView.as_view(), name="people_list"),
    path("people/<int:pk>/", PersonDetailView.as_view(), name="person_details"),
    path("addresses/", AddressListView.as_view(), name="address_list"),
    path("addresses/<int:pk>/", AddressDetailView.as_view(), name="address_details"),
    path("addresses/<int:pk>/edit", AddressUpdateView.as_view(), name="update_address"),
    path("addresses/<int:pk>/delete", AddressDeleteView.as_view(), name="delete_address"),
    path("addresses/create/", AddressCreateView.as_view(), name="create_address"),
]
