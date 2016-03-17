# Core django imports
from django.views.generic.base import TemplateView
from django.contrib import auth, messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.context_processors import csrf

# project specific imports
from blist_ui.forms import *  # __all__


class LandingView(TemplateView):
    """
    This is the default landing view, for guest users
    """
    template_name = 'landing.html'


class IndexView(TemplateView):
    """
    This is the default landing view, for logged in users
    """
    template_name = 'index.html'


class LogInView(TemplateView):
    '''This is the default landing view, for guest users'''
    template_name = 'landing.html'
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            auth.login(request, user)
            request.session['django_language'] = 'en'
            if not user.is_active:
                msg = ("You haven't yet verified your account. Please check your email "
                       "for instructions on how to do this. (May have accidentally ended "
                       "up in spam) <br />"
                       "This is necessary for you to receive job alerts")
                messages.info(request, msg)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.info(request, "Invalid Login Details provided." + str(form.errors))
            return HttpResponseRedirect(reverse('landing'))



class SignUpView(TemplateView):

    '''View defined for user signup.'''

    template_name = 'landing.html'

    def post(self, request, *args, **kwargs):

        usersignupform = UserSignupForm(request.POST)
        # get the user email address
        email = request.POST.get('email')
        new_user_signup = User.objects.filter(email__exact=email)

        # run if user already exist
        if new_user_signup:
            args = {}
            args.update(csrf(request))
            messages.info(request, "Email already taken please signup with another email.")
            return render(request, self.template_name, args)

        # run if user doesn't exist
        if usersignupform.is_valid():
            usersignupform.save()
            confirmation_msg = """You have sucessfully registered,
             please sign in."""
            messages.add_message(request, messages.INFO, confirmation_msg)
            return HttpResponseRedirect(reverse_lazy('signup'))

        # run if the first two conditions are not met.
        else:
            args = {}
            args.update(csrf(request))
            messages.info(request, "Fix the following errors:" + str(usersignupform.errors))
            return render(request, self.template_name, args)
