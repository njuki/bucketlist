# Import Django core libraries
from django.conf.urls import url, patterns, include

# App specific imports
from blist_ui import views as ui_views

# Generic URLs definition
urlpatterns = [
   url(r'^$', ui_views.LandingView.as_view(), name='landing'),
   url(r'^docs/', include('rest_framework_swagger.urls')),
]

# UI URLS
urlpatterns += [
    url(r'^', include('blist_ui.urls'))
]

# API URLS
urlpatterns += [
    url(r'^', include('blist_api.urls'))
]
