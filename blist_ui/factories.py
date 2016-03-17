#Third party imports
import factory

from .models import User

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    FACTORY_DJANGO_GET_OR_CREATE = ('username',)

    username = 'test_user'
    first_name = 'John'
    last_name = 'Doe'
    is_staff = False
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', 'default')