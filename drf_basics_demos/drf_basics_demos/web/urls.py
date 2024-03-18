from django.http import HttpResponse
from django.urls import path

from drf_basics_demos.web.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)

'''
resource located at /api/books/

# Server-side rendering

C => POST /api/books/create/ (GET /api/books/create/ for HTML of the form)
R => GET /api/books/ or GET /api/books/2/
U => POST /api/books/update/2/ (GET /api/books/update/ for HTML of the form)
D => POST /api/books/delete/2/ (GET /api/books/delete/ for HTML of the form)

# RESTful API:
C         => POST   /api/books/
R all     => GET    /api/books/

R details => GET    /api/books/2/
U         => PUT    /api/books/2/
D         => DELETE /api/books/2/

# `4` is the ID of the book? Wrong:
POST /api/comments/4

# `/reviews` is a REST **action**
POST /api/books/4/reviews
GET /api/books/4/reviews

# query params
# `/books?author=1


'''
