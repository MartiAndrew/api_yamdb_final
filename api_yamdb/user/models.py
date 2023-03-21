from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


from .enums import UserRole
from .consts import SERVICE_NAME


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name="Биография",
    )
    role = models.CharField(
        max_length=100,
        default=UserRole.USER,
        choices=UserRole.choices,
        verbose_name="Роль",
    )

    def clean(self):
        if self.username.lower() == SERVICE_NAME:
            raise ValidationError(
                f"Использовать {SERVICE_NAME} в качестве username запрещено."
            )

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
