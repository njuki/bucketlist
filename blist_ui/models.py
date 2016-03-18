from django.db import models
from django.contrib.auth.models import User
from wheel.metadata import unique


class Status(models.Model):
    """
    This model holds various statuses a bucket list item could be in.
    """
    name = models.CharField(
                            unique=True,
                            verbose_name="List Item Name",
                            max_length=100
                                         )
    description = models.TextField(
                                   blank=True,
                                   verbose_name="Description"
                                   )
    user = models.ForeignKey(User, null=True,
                                    verbose_name="Inserted By",
                                    related_name="State_inserted_by"
                                    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
     
    def __unicode__(self):
        return self.name
    
    
class Bucketlist((models.Model)):
    """
    This model holds various Buckets for different users.
    """
    name = models.CharField(
                            max_length=100,
                            unique=True,
                            verbose_name="" 
                            )
    description = models.TextField(
                                   blank=True,
                                   verbose_name=""
                                   )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="users")
    
    
    def get_list_items(self):
        return BucketlistItem.objects.filter(bucketlist=self)

    def __unicode__(self):
        return "Bucketlist: %s user: %s" % (self.name, self.user)

    class Meta:
        ordering = ("-date_created",)
    


class BucketlistItem(models.Model):
    """
    This defines BucketlistItems.
    """
    name = models.CharField(
                            max_length=100,
                            verbose_name="",
                            unique=True
                            )
    description = models.TextField(
                                   blank=True,
                                   verbose_name=""
                                   )
    bucketlist = models.ForeignKey(
                                   Bucketlist,
                                   related_name="items"
                                   )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, related_name="statuses")
    

    def __unicode__(self):
        return "BucketlistItem: %s" % (self.name)

    class Meta:
        ordering = ("-date_created",)