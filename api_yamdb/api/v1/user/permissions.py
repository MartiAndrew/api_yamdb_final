from rest_framework import permissions

from user.enums import UserRole


class AdminUserOrReadOnly(permissions.BasePermission):
    message = (f"Доступно только для всех пользователей с безопасными "
               f"запросами или утентифицированных пользователей с ролью "
               f"{UserRole.ADMIN} для остальных запросов.")

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.role == UserRole.ADMIN
        return False


class AdminPermission(permissions.BasePermission):
    message = f"Доступно только для пользователей с ролью {UserRole.ADMIN}"

    def has_permission(self, request, view):
        if not hasattr(request.user, "role"):
            return False

        return request.user.role == UserRole.ADMIN or request.user.is_superuser


class IsAuthorModeratorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.role in (UserRole.MODERATOR, UserRole.ADMIN))
