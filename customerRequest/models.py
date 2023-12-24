from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from django.db import models


class CustomerRequest(models.Model):
    service_type = models.CharField(max_length=255)
    number_of_users = models.IntegerField()
    about_platform = models.TextField()
    request_description = models.TextField()
    expected_date = models.DateTimeField()
    offer = models.PositiveIntegerField(blank=True, null=True)
    anything_else = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default='Initiation')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name  


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name
    

class Schedule(models.Model):
    ACTIVITY_CHOICES = [
    ('meeting', 'Meeting'),
    ('call', 'Call'),
    ('email', 'Email'),
    ]
    activity_type = models.CharField(max_length=255, choices=ACTIVITY_CHOICES)
    due_date = models.DateTimeField()
    summary = models.TextField(null=True, blank=True)
    fee = models.TextField(max_length=255)
    request = models.OneToOneField(CustomerRequest, on_delete=models.CASCADE, related_name='schedule')