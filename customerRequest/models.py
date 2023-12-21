from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from django.db import models

# class CustomUser(AbstractUser):
#     is_fraud = models.BooleanField(default=False)
#     groups = models.ManyToManyField(Group, related_name='customuser_set')

#     # Define a unique related_name for the user_permissions field
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='customuser_set'
#     )
#     def __str__(self):
#         return self.username

class CustomerRequest(models.Model):
    service_type = models.CharField(max_length=255)
    number_of_users = models.IntegerField()
    about_platform = models.TextField()
    request_description = models.TextField()
    expected_date = models.DateTimeField()
    anything_else = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='request')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='Initiation')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status  


class Company(models.Model):
    INDUSTRY_CHOICES = [
    ('IT', 'Information Technology'),
    ('finance', 'Finance'),
    ('healthcare', 'Healthcare'),
    ('business', 'Business')
    ]
    ETH = 'ETH'
    COUNTRY_CHOICES = [
        (ETH, 'Ethiopia')
    ]
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=255)
    phone = models.IntegerField()
    tin_number = models.IntegerField()
    business_classification = models.CharField(max_length=255)
    industry = models.TextField(max_length=255, choices=INDUSTRY_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name