from django.conf.urls import patterns, url

urlpatterns = patterns(
   '',
   url(r'^auth/login$', 'login', name='get-token'),
)