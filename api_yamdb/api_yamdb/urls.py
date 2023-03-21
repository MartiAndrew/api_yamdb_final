from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from rest_framework import permissions

DEFAULT_VERSION = 'v1'


schema_view = get_schema_view(
    openapi.Info(
        title='Yamdb API',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path('admin/', admin.site.urls),
    path('redoc/',
         TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
    path(f'api/{DEFAULT_VERSION}/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
