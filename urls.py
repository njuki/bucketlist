# Import Django core libraries
from django.conf.urls import url, patterns, include

# App specific imports
from blist_ui import views as ui_views

# Generic URLs definition
urlpatterns = patterns(
   '',
   url(r'^$', ui_views.LandingView.as_view(), name='landing'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)

# UI URLS
urlpatterns += patterns(
    '',
    url(r'^', include('blist_ui.urls'))
)

# API URLS
urlpatterns += patterns(
    '',
    url(r'^', include('blist_api.urls'))
)
