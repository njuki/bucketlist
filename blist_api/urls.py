from django.conf.urls import patterns, url
from blist_api import views as api_views

urlpatterns = patterns(
   '',
    url(r'^auth/login$', api_views.GetAuthenticationToken.as_view(), name='get-token'),
)