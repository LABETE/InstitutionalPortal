from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic import RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Debt
from .forms import DebtForm


class DebtDetailView(LoginRequiredMixin, DetailView):
    model = Debt
    slug_field = 'id'
    slug_url_kwarg = 'id'


class DebtRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('debts:detail', kwargs={'id': self.id})


class DebtCreateView(LoginRequiredMixin, CreateView):
    model = Debt
    form_class = DebtForm

    def get_success_url(self):
        return reverse('debts:list')


class DebtUpdateView(LoginRequiredMixin, UpdateView):
    model = Debt
    form_class = DebtForm
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get_succesful_url(self):
        return reverse('debts:detail', kwargs={'pk': self.object.pk})

    def get_object(self):
        return Debt.objects.get(pk=self.object.pk)


class DebtListView(LoginRequiredMixin, ListView):
    model = Debt
    slug_field = 'id'
    slug_url_kwarg = 'id'
