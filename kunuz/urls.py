from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from debug_toolbar.toolbar import debug_toolbar_urls

schema_view = get_schema_view(
    openapi.Info(
        title='kun.uz API',
        default_version='v1',
        description='description',
        terms_of_service="terms",
        contact=openapi.Contact(email="SUIII@gmail.com"),
        license=openapi.License(name="GDAGIDIGIDIGIDAO"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('common.urls')),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + debug_toolbar_urls()


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

