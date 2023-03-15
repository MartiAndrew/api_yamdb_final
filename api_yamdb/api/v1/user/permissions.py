from rest_framework import permissions
from user.enums import UserRole


class AdminPermission(permissions.BasePermission):
    message = "Имеет права админа"

    def has_permission(self, request, view):
        if not hasattr(request.user, "role"):
            return False

        return request.user.role == UserRole.ADMIN or request.user.is_superuser


class ModeratorPermission(permissions.BasePermission):
    message = "Имеет права модератора"

    def has_permission(self, request, view):
        return (
            request.user.role == UserRole.MODERATOR
            or request.user.is_superuser,
        )
