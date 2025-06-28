from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Teknohole API",
        default_version='v1',
        description="Dokumentasi REST API Teknohole",
        contact=openapi.Contact(email="teknohole@gmail.com"),
    ),
    public=True,
    # permission_classes=[IsSwaggerAllowed],
    authentication_classes=[SessionAuthentication],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth', include('auth.urls')),
    path('api/profil', include('profil.urls')),
    path('api/madrasah', include('madrasah.urls')),
    path('api/akademik', include('akademik.urls')),
    path('api/pengumuman', include('pengumuman.urls')),

    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
