from operator import is_
from tabnanny import verbose
import uuid
from django.db import models

# Create your models here.

class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    social_name = models.CharField(max_length=255)
    nif = models.CharField(max_length=16, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address_street = models.CharField(max_length=255, null=True, blank=True)
    address_number = models.CharField(max_length=100, null=True, blank=True)
    address_city = models.CharField(max_length=255, null=True, blank=True)
    address_state = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'business'
        ordering = ['id']
        verbose_name = 'business'
        verbose_name_plural = 'businesses'

    def __str__(self):
        return self.social_name
