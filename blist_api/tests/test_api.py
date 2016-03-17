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
        self.user = factories.UserFactory()
        
    
    def test_authorized_access(self):
        """Tests that only authenticated users can access the endpoint"""

        # should fail for non-logged in user
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 401)
