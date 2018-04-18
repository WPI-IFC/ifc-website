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
        regex=r'^chapter/$',
        view=RedirectView.as_view(pattern_name="events-index", permanent=False)
    ),
    url(
        regex=r'^officers/new/$',
        view=views.new_officer_event,
        name="event-officer-new"
    ),
    url(
        regex=r'^chapter/(?P<chapter>[\D]+)/new/$',
        view=views.new_chapter_event,
        name="event-chapter-new"
    ),
    url(
        regex=r'^chapter/(?P<chapter>[\D]+)/$',
        view=RedirectView.as_view(pattern_name="events-index", permanent=False)
    ),
    url(
        regex=r'^officers/(?P<event_id>[\d]+)/$',
        view=views.officer_event_info,
        name="event-officer-overview"
    ),
    url(
        regex=r'^chapter/(?P<event_id>[\d]+)/$',
        view=views.chapter_event_info,
        name="event-chapter-overview"
    ),
]