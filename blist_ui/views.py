#Import Django core libraries
from django.views.generic.base import TemplateView

class LandingView(TemplateView):
    """
    This is the default landing view, for guest users
    """
    template_name = 'landing.html'
