#3rd party imports
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions

# Django core imports
from django.http import Http404
from django.shortcuts import get_object_or_404

# project specific imports
from blist_ui.models import Bucketlist, BucketlistItem
from .serializers import BucketListSerializer, BucketlistItemSerializer
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
    

class BucketListView(APIView):
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


class BucketListDetailView(GenericAPIView):
    """Retrieves, updates or deletes a Bucketlist instance."""
    
    model = Bucketlist
    serializer_class = BucketListSerializer
    pagination_class = PageLimit

    def get_object(self, pk):
        bucket_object = get_object_or_404(Bucketlist, pk=pk)
        return bucket_object
        

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
    

class BucketListItemView(GenericAPIView):
    """Adds an Item to a selected Buckectlist for a given user."""

    serializer_class = BucketlistItemSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageLimit
    

    def post(self, request, id):

        bucketlist = get_object_or_404(Bucketlist, pk=id)
        
        itemserializer = BucketlistItemSerializer(data=request.data)
        bucketserializer = BucketListSerializer(bucketlist)
        
        if itemserializer.is_valid():
            itemserializer.save()
            return Response(bucketserializer.data,
                            status=status.HTTP_201_CREATED)
            
        return Response(
            itemserializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        

class ItemListDetailView(GenericAPIView):
    """Deletes and Updates bucketlist item having the given id."""

    serializer_class = BucketlistItemSerializer
    pagination_class = PageLimit

    def put(self, request, id, item_id):

        get_object_or_404(Bucketlist, pk=id)
        item = get_object_or_404(BucketlistItem, pk=id)

        itemserializer = BucketlistItemSerializer(item, data=request.data)
        if itemserializer.is_valid():
            itemserializer.save()
            return Response(itemserializer.data,
                            status=status.HTTP_200_OK)
            
        return Response(itemserializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, item_id):

        item = get_object_or_404(BucketlistItem, pk=item_id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)