from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name='driver_set',  # Unique related_name for the groups field
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='driver_permissions_set',  # Unique related_name for the user_permissions field
        blank=True
    )

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="cars", blank=True, null=True)

    def __str__(self):
        return self.model
