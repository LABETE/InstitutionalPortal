from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.DebtListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^redirect/$',
        view=views.DebtRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<id>[\d]+)/$',
        view=views.DebtDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^update/$',
        view=views.DebtUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^create/$',
        view=views.DebtCreateView.as_view(),
        name='create'
    ),
]
