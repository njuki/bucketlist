from rest_framework import serializers

from blist_ui.models import Bucketlist, BucketlistItem

class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'user', 'description', 'date_created', 'date_modified')

    def __init__(self, *args, **kwargs):
        """
        Control which fields to be shown
        """
        # Pop the 'fields' arg
        fields = kwargs.pop('fields', None)

        # Instantiate the super class
        super(BucketListSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
                
                
class BucketlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketlistItem
        fields = ('id', 'name', 'description', 'bucketlist', 'status', 'date_created', 'date_modified')

    def __init__(self, *args, **kwargs):
        """
        Control which fields to be shown
        """
        # Pop the 'fields' arg
        fields = kwargs.pop('fields', None)

        # Instantiate the super class
        super(BucketlistItemSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

