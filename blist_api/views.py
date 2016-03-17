#3rd party imports
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions

# project specific imports
from blist_ui.models import Bucketlist
from blist_api.serializers import BucketListSerializer


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
    

class BucketList(APIView):
    """ Adds or Lists Buckectlists for a given user."""
    
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        """List all Buckets belonging to the logged in user."""
        
        lists = Bucketlist.objects.all()
        serializer = BucketListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Creates a new Bucketlist belonging to the logged in user."""
        
        serializer = BucketListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)