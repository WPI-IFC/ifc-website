from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.event_index,
        name="events-index"
    ),
    url(
        regex=r'^(?P<event_id>[\d]+)/$',
        view=views.event_info,
        name="event-overview"
    ),
]