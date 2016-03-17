#3rd party imports
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class AuthenticationTokenView(GenericAPIView):
    
    """Gets token from a post request. On receiving valid username and password, the class
      attempts to fetch the token associated with that user. If not found a new
      token is created.
    """
    
    permission_classes = ()
    serializer_class = AuthTokenSerializer

    def post(self, request):
        """
          The post expects the payoload to contain a valid username and passoword.
          The auth token associated with the user is return is json format.
        """
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token[0].key})