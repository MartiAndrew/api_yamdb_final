from django.urls import include, path
from rest_framework import routers

from .v1.user.view import UserViewSet, UserMeAPIView
from .v1.auth.view import SignUpAPIView, TokenAPIView
from .views import TitleViewSet

router = routers.DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("users/me/", UserMeAPIView.as_view(), name="user_me"),
    path("auth/signup/", SignUpAPIView.as_view(), name="signup"),
    path("auth/token/", TokenAPIView.as_view(), name="token"),
]
