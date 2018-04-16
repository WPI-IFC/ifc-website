from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.officer_index,
        name="officers-index"
    ),
    # Django url matching is wonky sometimes
    # we need to put this url before the base one
    # so it routes properly.
    url(
        regex=r'^(?P<slug>[\D]+)/new/$',
        view=views.new_post,
        name="officers-new-post"
    ),
    url(
        regex=r'^(?P<slug>[\D]+)/$',
        view=views.position_overview,
        name="officers-overview"
    ),
    url(
        regex=r'^(?P<slug>[\D]+)/(?P<id>[\d]+)/$',
        view=views.get_post,
        name='officers-view-post'
    ),
    url(
        regex=r'^(?P<slug>[\D]+)/(?P<id>[\d]+)/edit/$',
        view=views.edit_post,
        name='officers-edit-post'
    ),
]