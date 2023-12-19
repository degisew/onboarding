from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    is_fraud = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='customuser_set')

    # Define a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_set'
    )
    def __str__(self):
        return self.username

class CustomerRequest(models.Model):
    service_type = models.CharField(max_length=255)
    number_of_users = models.IntegerField()
    about_platform = models.TextField()
    request_description = models.TextField()
    expected_date = models.DateTimeField()
    anything_else = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='Initiation')
    updated_at = models.DateTimeField(auto_now=True)


