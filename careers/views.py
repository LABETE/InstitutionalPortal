from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic import RedirectView, DetailView

from braces.views import LoginRequiredMixin

from .models import Career
from .forms import CareerForm


class CareerDetailView(LoginRequiredMixin, DetailView):
    model = Career
    slug_field = "code"
    slug_url_kwarg = "code"


class CareerRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("careers:detail", kwargs={"code": self.object.code})


class CareerCreateView(LoginRequiredMixin, CreateView):
    model = Career
    form_class = CareerForm
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_success_url(self):
        return reverse("careers:list")


class CareerUpdateView(LoginRequiredMixin, UpdateView):
    model = Career
    form_class = CareerForm

    def get_success_url(self):
        return reverse("careers:list")

    def get_object(self):
        return Career.objects.get(code=self.kwargs['code'])


class CareerListView(LoginRequiredMixin, ListView):
    model = Career
    slug_field = "code"
    slug_url_kwarg = "code"
