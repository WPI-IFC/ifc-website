from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^/$',
        view=views.index,
        name='house-info'
    ),
    url(
        regex=r'^/(?P<house>[\D]+)/$',
        view=views.house_info,
        name='house-landing'
    )
]