from django.contrib import admin
from django.urls import path
from .views import ApiEndpoint

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Endpoint",
      default_version='v1',
      description="This is a web scraping project. You can search for real estate property in Malaysia. Just enter any location/area that you preferred and we will render the list for you!",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('',  schema_view.with_ui('swagger', cache_timeout=0), name='home'),
    path('run/', ApiEndpoint.as_view(), name='run'),
    path('admin/', admin.site.urls),
]

