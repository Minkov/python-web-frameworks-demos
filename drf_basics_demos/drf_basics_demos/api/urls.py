from django.urls import path

from drf_basics_demos.api.views import api_list_books, BookListApiView, BookUpdateApiView

urlpatterns = (
    path("books/", BookListApiView.as_view(), name="api_list_create_books"),
    path("books/<int:pk>/", BookUpdateApiView.as_view(), name="api_book_update"),
)
