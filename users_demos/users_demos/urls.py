from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users_demos.auth_app.urls')),
    path('', include('users_demos.web.urls')),
]
