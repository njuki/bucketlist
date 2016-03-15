#3rd party imports
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.
class GetAuthenticationToken(GenericAPIView):
    
    """Get token on login."""
    
    permission_classes = ()
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})