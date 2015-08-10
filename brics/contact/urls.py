from django.conf.urls import patterns, url

from .views import ContactView

urlpatterns = patterns(
    '',
    url(
        r'^contact',
        ContactView.as_view(),
        name='contact'
    ),
)
