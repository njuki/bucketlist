from django.conf.urls import url
from blist_api import views as api_views

urlpatterns = [
    url(r'^auth/login$', api_views.AuthenticationTokenView.as_view(),
        name='token-auth'),
    url(r'^bucketlists/$', api_views.BucketList.as_view(), name='bucket-list'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', api_views.BucketListDetail.as_view(),
        name='bucket-list-details'),
     url(r'^bucketlists/(?P<id>[0-9]+)/items/$', api_views.BucketListItem.as_view(),
        name='bucket-list-item'),
    url(r'^bucketlists/(?P<id>[0-9]+)/items/(?P<item_id>[0-9]+)$',
        api_views.ItemListDetail.as_view(),
        name='list-item-details'),
]