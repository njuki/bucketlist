from django.conf.urls import patterns, url
from blist_api import views as api_views

urlpatterns = [
    url(r'^auth/login$', api_views.AuthenticationTokenView.as_view(), name='get-token'),
    url(r'^bucketlists/$', api_views.BucketList.as_view(), name='bucket-list'),
]