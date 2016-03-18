# Core django imports
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import auth, messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.context_processors import csrf

# project specific imports
from blist_ui.forms import *  # __all__
from blist_ui.models import Bucketlist, BucketlistItem, Status
from blist_ui.forms.forms import BucketlistForm


class LandingView(TemplateView):
    """
    This is the default landing view, for guest users.
    """
    
    template_name = 'landing.html'


class LogInView(TemplateView):
    """ Login view."""
    
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
        

class IndexView(ListView):
    """
    This is the default landing view, for logged in users
    """
    template_name = 'partials/bucketlist.html'
    model = Bucketlist
    

class BucketlistCreate(CreateView):
    template_name = "create.html"
    model = Bucketlist
    form_class = BucketlistForm
    success_url = '/home'
    
    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        return super(BucketlistCreate, self).form_valid(form_class)
    

class BucketlistUpdate(UpdateView):
    template_name = 'update.html'
    fields = ['name', 'description']
    model = Bucketlist
    success_url = '/home'
    

class BucketlistDelete(DeleteView):
    template_name = 'delete.html'
    model = Bucketlist
    
    def get_success_url(self):
        return reverse_lazy('home')
    

class BucketlistItemCreate(CreateView):
    template_name = "create.html"
    model = BucketlistItem
    form_class = BucketlistItemForm
    success_url = '/home'
    
    def form_valid(self, form_class):
        status = Status.objects.get(pk=1)
        form_class.instance.status = status
        form_class.instance.bucketlist = Bucketlist.objects.get(pk=self.kwargs['bid'])
        return super(BucketlistItemCreate, self).form_valid(form_class)
    
class BucketlistItemUpdate(UpdateView):
    template_name = 'update.html'
    fields = ['name', 'description', 'status']
    model = BucketlistItem
    success_url = '/home'
    

class BucketlistItemDelete(DeleteView):
    template_name = 'delete.html'
    model = BucketlistItem
    
    def get_success_url(self):
        return reverse_lazy('home')
        
