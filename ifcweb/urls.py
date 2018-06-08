"""ifcweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r'^about/officer/', include('officers.urls')),
    url(r'^about/$', views.about),
    url(r'^chapters/', include('houses.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^change_password/$', auth_views.password_change, {'template_name': 'pass_change.html'}, name='change-password'),
    url(r'^change_password/done/$', auth_views.password_change_done, {'template_name': 'pass_change_done.html'}, name='password_change_done'), # Django-required reverse name
    url(r'^events/', include('events.urls')),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}),
    url(r'^style/', views.style, name="style-example"),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)