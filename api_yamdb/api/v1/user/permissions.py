from rest_framework import permissions
from user.enums import UserRole


class AdminPermission(permissions.BasePermission):
    message = f"Доступно только для пользователей с ролью {UserRole.ADMIN}"

    def has_permission(self, request, view):
        if not hasattr(request.user, "role"):
            return False

        return request.user.role == UserRole.ADMIN or request.user.is_superuser


class ModeratorRole(permissions.BasePermission):
    message = f"Доступно только для пользователей с ролью {UserRole.MODERATOR}"

    def has_permission(self, request, view):
        return (request.user.role == UserRole.MODERATOR or request.user.is_superuser,)
