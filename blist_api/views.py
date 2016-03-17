#3rd party imports
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions

# Django core imports
from django.http import Http404

# project specific imports
from blist_ui.models import Bucketlist
from .serializers import BucketListSerializer
from .pagination import PageLimit


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
        return Response({'token': token[0].key, 'user_id': user.id})
    

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


class BucketListDetail(GenericAPIView):
    """Retrieves, updates or deletes a Bucketlist instance."""
    
    model = Bucketlist
    serializer_class = BucketListSerializer
    pagination_class = PageLimit

    def get_object(self, pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """This gets a single bucket list."""
        
        bucketlist = self.get_object(pk)
        serializer = BucketListSerializer(bucketlist)
        return Response(serializer.data)

    def put(self, request, pk):
        """This updates the bucketlist with `id`=pk."""
        
        bucketlist = self.get_object(pk)

        serializer = BucketListSerializer(
            bucketlist,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """This deletes the bucketlist with `id`=pk."""
        
        bucketlist = self.get_object(pk)

        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)