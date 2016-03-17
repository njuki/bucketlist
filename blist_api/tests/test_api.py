"""
Bucketlist app API Tests Suite
"""

__author__ = "Josiah Njuki <jnjuki103@gmail.com>"
__copyright__ = "Copyright 2016, Andel"
__date__ = "Thur 17th Mar 2016"

from rest_framework.test import APITestCase

from django.core.urlresolvers import reverse

# Local application imports
from blist_ui import factories



class BucketListTestCase(APITestCase):
    """Tests the Bucket list API authentication, creating and listing."""
    
    def setUp(self):
        self.bucketlist_url = reverse("bucket-list")
        self.auth_url = reverse("token-auth")
        self.user_factory = factories.UserFactory()
        
    
    def test_authorized_access(self):
        """Tests that only authenticated users can access the endpoint"""

        # Should fail for non-logged in user
        response = self.client.get(self.bucketlist_url)
        self.assertEqual(response.status_code, 401)

        response = self.client.post(self.bucketlist_url)
        self.assertEqual(response.status_code, 401)
        
        # Get auth_token
        credentials = {
                       "username": self.user_factory.username,
                       "password": "default"
        }
        
        response = self.client.post(self.auth_url, data=credentials)
        auth_token = response.data['token']
        
        # Use the auth_token obtained to access authenticate on the endpoint
        self.client.credentials(HTTP_AUTHORIZATION="Token " + auth_token)
        
        # Should go through since the token is valid
        response = self.client.get(self.bucketlist_url)
        self.assertEqual(response.status_code, 200)
        
        # Authenitcation should pass but then fail with a bad request response
        response = self.client.post(self.bucketlist_url)
        self.assertEqual(response.status_code, 400)
        
    def test_add_bucketlist(self):
        """
        Tests that an authenticated user can create a new bucketlist via a post
        to the bucketlist endpoint
        """
        
        credentials = {
                       "username": self.user_factory.username,
                       "password": "default"
        }
        
        response = self.client.post(self.auth_url, data=credentials)
        auth_token = response.data['token']
        user_id = response.data['user_id']
       
        self.client.credentials(HTTP_AUTHORIZATION="Token " + auth_token)
        bucketlist_payload = {
                       "name": "BuckList1",
                       "description": "Test Description",
                       "user": user_id
        }
        
        # test post successful
        response = self.client.post(self.bucketlist_url, data=bucketlist_payload)
        self.assertEqual(response.status_code, 201)
        
    def test_update_delete_bucketlist(self):
        """
        Tests that an authenticated user can update a existing bucketlist.
        """
        
        credentials = {
                       "username": self.user_factory.username,
                       "password": "default"
        }
        
        response = self.client.post(self.auth_url, data=credentials)
        auth_token = response.data['token']
        user_id = response.data['user_id']
       
        self.client.credentials(HTTP_AUTHORIZATION="Token " + auth_token)
        bucketlist_payload = {
                       "name": "BuckList1",
                       "description": "Test Description",
                       "user": user_id
        }
        
        """Create a backet list then update it."""
        
        response = self.client.post(self.bucketlist_url, data=bucketlist_payload)
        
        update_url = reverse("bucket-list") + str(response.data['id']) + "/"
        
        # Update the created bucketlist
        update_payload =  {
                       "name": "BuckList1 Edited",
                       "description": "Test Description Edited",
                        "user": user_id
        }
        # Test update successful
        response = self.client.put(update_url, data=update_payload)
        
        # response should be a 200
        self.assertEqual(response.status_code, 200)
        
        # Now test delete
        response = self.client.delete(update_url)

        # response should be a 204
        self.assertEqual(response.status_code, 204)
        
