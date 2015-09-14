from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.CareerListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^redirect/$',
        view=views.CareerRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<code>[\w-]+)/$',
        view=views.CareerDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<code>[\w-]+)/update/$',
        view=views.CareerUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^create/$',
        view=views.CareerCreateView.as_view(),
        name='create')
]
