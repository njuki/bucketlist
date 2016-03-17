from django.conf.urls import patterns, url
from blist_ui import views as ui_views

urlpatterns = [
    url(r'^login/', ui_views.LogInView.as_view(), name='login'),
    url(r'^signup/', ui_views.SignUpView.as_view(), name='signup'),
    url(r'^home/', ui_views.IndexView.as_view(), name='home'),
]