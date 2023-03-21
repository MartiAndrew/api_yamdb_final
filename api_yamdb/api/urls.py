from django.urls import include, path
from rest_framework import routers

from .v1.user.view import UserViewSet, UserMeAPIView
from .v1.auth.view import SignUpAPIView, TokenAPIView
from .v1.genre.views import GenreViewSet
from .v1.category.views import CategoryViewSet
from .v1.title.views import TitleViewSet
from .v1.review.views import ReviewViewSet
from .v1.comment.views import CommentViewSet

router = routers.DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(r'users', UserViewSet, basename='user')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')


urlpatterns = [
    path('users/me/', UserMeAPIView.as_view(), name='user_me'),
    path('auth/signup/', SignUpAPIView.as_view(), name='signup'),
    path('auth/token/', TokenAPIView.as_view(), name='token'),
    path('', include(router.urls)),
]
