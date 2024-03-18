from django.urls import path
from rest_framework.authtoken import views as token_views

from drf_basics_demos.api.views import api_list_books, BookListCreateApiView, BookUpdateApiView, api_list_authors, \
    LoginApiView, RegisterApiView

urlpatterns = (
    path("books/", BookListCreateApiView.as_view(), name="api_list_create_books"),
    path("books/<int:pk>/", BookUpdateApiView.as_view(), name="api_book_update"),
    path("authors/", api_list_authors, name="api_list_authors"),
    path("accounts/token/", LoginApiView.as_view(), name="api_obtain_auth_token"),
    path("accounts/", RegisterApiView.as_view(), name="api_user_create"),
)
