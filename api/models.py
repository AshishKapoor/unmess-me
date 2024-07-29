from django.db import models


# Create your models here.
from django.db import models

class InteriorDesigner(models.Model):
    # Basic information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Professional information
    years_of_experience = models.PositiveIntegerField()
    specialties = models.CharField(max_length=255, help_text="Comma-separated list of specialties")
    bio = models.TextField(blank=True, null=True)

    # Portfolio
    website = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True, help_text="Link to portfolio")

    # Availability and status
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Interior Designer"
        verbose_name_plural = "Interior Designers"

