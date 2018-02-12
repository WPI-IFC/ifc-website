from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.event_index,
        name="events-index"
    ),
    url(
        regex=r'^officers/$',
        view=RedirectView.as_view(pattern_name="events-index", permanent=False)
    ),
    url(
        regex=r'^houses/$',
        view=RedirectView.as_view(pattern_name="events-index", permanent=False)
    ),
    url(
        regex=r'^officers/(?P<event_id>[\d]+)/$',
        view=views.officer_event_info,
        name="event-officer-overview"
    ),
    url(
        regex=r'^houses/(?P<event_id>[\d]+)/$',
        view=views.house_event_info,
        name="event-houses-overview"
    ),
]