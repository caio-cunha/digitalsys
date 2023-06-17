from django.urls import include, path
from loans.api import urls
from .views import index

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="System Sys API",
        default_version='v1',
        description="Manage Loans",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="caiocomputacao2014@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(urls)),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]