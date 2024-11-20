from django.contrib.auth.models import Group, Permission
from django.db import models

class users(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('manager', 'Gerente'),
        ('seller', 'Cambista'),
        ('client', 'Cliente'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True
    )

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return f"{self.username}"
