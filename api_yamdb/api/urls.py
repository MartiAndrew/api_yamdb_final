from django.urls import include, path
from rest_framework import routers

from .v1.user.view import UserViewSet, UserMeAPIView
from .v1.auth.view import SignUpAPIView, TokenAPIView
from .v1.genre.views import GenreViewSet
from .v1.category.views import CategoryViewSet
from .v1.title.views import TitleViewSet

router = routers.DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/me/', UserMeAPIView.as_view(), name='user_me'),
    path('auth/signup/', SignUpAPIView.as_view(), name='signup'),
    path('auth/token/', TokenAPIView.as_view(), name='token'),
    path('', include(router.urls)),
]
