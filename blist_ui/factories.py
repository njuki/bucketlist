#Third party imports
import factory

from .models import User, Bucketlist, Status

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    FACTORY_DJANGO_GET_OR_CREATE = ('username',)

    username = 'test_user'
    first_name = 'John'
    last_name = 'Doe'
    is_staff = False
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', 'default')
    

class BucketlistFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Bucketlist
    FACTORY_DJANGO_GET_OR_CREATE = ('name',)

    name = 'BuckList1'
    description = 'Test Description'
    user = factory.SubFactory(UserFactory)
    
class StatusFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Status
    FACTORY_DJANGO_GET_OR_CREATE = ('name',)

    name = 'Pending'
    description = 'Pending Action'
    user = factory.SubFactory(UserFactory)