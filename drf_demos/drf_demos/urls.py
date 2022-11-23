from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Enables browsable API of DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('drf_demos.api.urls')),
    path('', include('drf_demos.web.urls')),
]
