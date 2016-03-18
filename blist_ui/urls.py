from django.conf.urls import url
from  django.contrib.auth import views
from blist_ui import views as ui_views

urlpatterns = [
    url(r'^login/', ui_views.LogInView.as_view(), name='login'),
    url(r'^login/', views.logout, name='logout'),
    url(r'^signup/', ui_views.SignUpView.as_view(), name='signup'),
    url(r'^home/', ui_views.IndexView.as_view(), name='home'),
    url(r'^bucketlist/create', ui_views.BucketlistCreate.as_view(),
        name='bucketlist-create'),
    url(r'^bucketlist/edit/(?P<pk>\d+)$', ui_views.BucketlistUpdate.as_view(), name='bucketlist-edit'),
    url(r'^bucketlist/delete/(?P<pk>\d+)$', ui_views.BucketlistDelete.as_view(), name='bucketlist-delete'),
    url(r'^bucketlistitem/create/(?P<bid>\d+)$', ui_views.BucketlistItemCreate.as_view(), name='bucketlistitem-add'),
    url(r'^bucketlistitem/edit/(?P<pk>\d+)$', ui_views.BucketlistItemUpdate.as_view(), name='bucketlistitem-edit'),
    url(r'^bucketlistitem/delete/(?P<pk>\d+)$', ui_views.BucketlistItemDelete.as_view(), name='bucketlistitem-delete'),
]
