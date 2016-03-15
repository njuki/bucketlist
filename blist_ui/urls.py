from django.conf.urls import patterns, url

urlpatterns = patterns(
   '',
   url(r'^login/', 'login', name='login'),
)