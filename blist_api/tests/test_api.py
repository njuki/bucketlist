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
        self.url = reverse("bucket-list")
        self.user_factory = factories.UserFactory()
        
    
    def test_authorized_access(self):
        """Tests that only authenticated users can access the endpoint"""

        # Should fail for non-logged in user
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 401)
        
        # Get auth_token
        auth_url = reverse("token-auth")
        credentials = {
                       "username": self.user_factory.username,
                       "password": "default"
        }
        
        response = self.client.post(auth_url, data=credentials)
        auth_token = response.data['token']
        
        # Use the auth_token obtained to access authenticate on the endpoint
        self.client.credentials(HTTP_AUTHORIZATION="Token " + auth_token)
        
        # Should go through since the token is valid
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        # Authenitcation should pass but then fail with a bad request response
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)
        
