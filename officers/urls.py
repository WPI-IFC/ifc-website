from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.officer_index,
        name="officers-index"
    ),
]