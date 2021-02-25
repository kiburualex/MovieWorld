"""movieworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


# ----- swagger configs ----
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # --- swagger urls ---
    # -- A JSON view of your API specification at /swagger.json or a YAML view at /swagger.yaml
    re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # -- A swagger-ui view of your API specification at /swagger/
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # -- A ReDoc view of your API specification at /redoc/
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('admin/', admin.site.urls),
    path('api/token/', obtain_jwt_token, name='jwt-auth'),
    path('api/refresh/', refresh_jwt_token, name='jwt-auth-refresh'),
    path('movies/', include('movies.urls'), name='movies'),
    path('users/', include('users.urls'), name='users'),
]