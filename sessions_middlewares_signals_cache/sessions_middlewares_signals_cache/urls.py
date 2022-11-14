from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sessions_middlewares_signals_cache.web.urls')),
]
