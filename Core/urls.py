from django.contrib import admin
from django.urls import path
from App.views import TurmodelListCreate, TurAdminView, TurAdminPK
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define schema view for Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="News API",
        default_version='v1',
        description="News App server",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sturayeva000@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', TurmodelListCreate.as_view(), name='turmodel-list-create'),
    path('create/', TurAdminView.as_view()),
    path('crud/{int:pk}/', TurAdminPK.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'), 
]
