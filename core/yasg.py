from django.conf import settings
from django.urls import re_path
from drf_yasg.generators import OpenAPISchemaGenerator

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title='Credit-card',
        default_version='v1',
        description='Credit-card API description',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dimas.kg93@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(settings.API_PERMISSION,),
)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
