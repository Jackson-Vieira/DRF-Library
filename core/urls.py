
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


from library.api.urls import router


# DOCUMENTAÇÃO SWAGGER
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Library API",
        default_version="1.0.0",
        description="API documentation of App",
    ),
    public = True,
)
   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include('library.urls')),

    # API
    path('api/v1/', include(router.urls)),

    # DOCUMENTAÇÃO 
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)