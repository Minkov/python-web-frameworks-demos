from django.contrib import admin
from django.urls import path

from middlewares_sessions_cookies_demos.web.views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
]

'''
HTTP is stateless

Client
        sends a request
                        server
                            receives a request
                                ....
                            returns a response
        receives the response

'''