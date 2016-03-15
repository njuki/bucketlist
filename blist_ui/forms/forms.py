# core django imports
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, max_length=75,
        widget = forms.TextInput())
    password = forms.CharField()

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not "username" in self._errors and not "password" in self._errors:
            username = cleaned_data.get("username")
            password = cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "Wrong Username and/or Password. Please try again.ss" + str(password))
            else:
                self.user = user
        return cleaned_data


class UserSignupForm(UserCreationForm):
    '''
    Field defined to override default field property.
    '''
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)

    class Meta:
        '''
        UserCreationform uses the django User object.
        '''
        model = User
        fields = ('full_name', 'email', 'password1', 'password2')
    
    def save(self):
        '''
        Save method used by the AbstractUser object.
        '''
        full_name = self.cleaned_data['full_name'].split( )
        user = User.objects.create_user(
            first_name = full_name[0],
            last_name =full_name[1],
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'])
        return user
