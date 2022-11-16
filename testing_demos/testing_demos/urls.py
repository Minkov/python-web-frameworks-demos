from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testing_demos.web.urls')),
    path('accounts/', include('testing_demos.accounts.urls')),
]
