from django.db import models

class CustomerRequest(models.Model):
    service_type = models.CharField(max_length=255)
    number_of_users = models.IntegerField()
    about_platform = models.TextField()
    request_description = models.TextField()
    expected_date = models.DateTimeField()
    anything_else = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


