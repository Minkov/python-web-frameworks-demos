import time

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from rest_framework import serializers, status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework import generics as api_generic_views
from rest_framework.authtoken import views as token_views

from django.views import generic as views
from rest_framework import views as api_views

from rest_framework.response import Response

from drf_basics_demos.api.models import Book, Author
from drf_basics_demos.api.permissions import IsOwnerPermission
from drf_basics_demos.api.serializers import AuthorForListSerializer, BookForListSerializer, BookForCreateSerializer


# class BookListApiView()

def list_books(request):
    book_list = Book.objects.all()

    context = {
        "book_list": book_list,
    }

    return render(request, "...", context)


@api_view(http_method_names=["GET"])
def api_list_authors(request):
    author_list = Author.objects.all()

    serializer = AuthorForListSerializer(author_list, many=True)

    return Response(data=serializer.data)


@api_view(http_method_names=("GET",))
def api_list_books(request):
    # `book_list` is Queryset of Book objects
    book_list = Book.objects.all()

    serializer = BookForListSerializer(book_list, many=True)

    json = serializer.data

    return Response(data=json)


class BookListView(views.CreateView):
    def get(self, request):
        return render(request, "")

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('...')

        return render(request, "...", context=None)


# class BookListApiView(api_views.APIView):
#     # queryset = Book.objects.all()
#     # serializer_class = BookSerializer
#
#     def get(self, request):
#         # time.sleep(3)
#         book_list = Book.objects.all()
#         serializer = BookForListSerializer(book_list, many=True)
#         json = serializer.data
#         return Response(data=json)
#
#     def post(self, request):
#         serializer = BookForListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookListCreateApiView(api_generic_views.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerPermission,
    ]

    # def get_permissions(self):
    #     if self.request.method == "POST":
    #         return [permissions.IsAuthenticated()]

    list_serializer_class = BookForListSerializer
    create_serializer_class = BookForCreateSerializer

    serializer_class = list_serializer_class

    def get_serializer_class(self):
        if self.request.method == "POST":
            return self.create_serializer_class
        return self.list_serializer_class

    def get(self, request, *args, **kwargs):
        time.sleep(3)
        return super().get(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     # apply filter
    #     title_pattern = self.request.query_params.get('title', None)
    #     if title_pattern:
    #         queryset = queryset.filter(title__icontains=title_pattern)
    #
    #     return queryset

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        title_pattern = self.request.query_params.get('title', None)
        if title_pattern:
            queryset = queryset.filter(title__icontains=title_pattern)

        return queryset


class BookUpdateApiView(api_views.APIView):
    def get_object(self, pk):
        return (Book.objects.filter(pk=pk)
                .first())

    def get(self, request, pk):
        serializer = BookForListSerializer(instance=self.get_object(pk))
        json = serializer.data
        return Response(data=json)

    def put(self, request, pk):
        serializer = BookForListSerializer(data=request.data, instance=self.get_object(pk))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Account

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


class RegisterApiView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer


# In Django
# class LoginView(LoginView)
class LoginApiView(token_views.ObtainAuthToken):
    pass

# No need. Handled on the client-side (React, Android,...)
# class LogoutApiView(generics.CreateAPIView):
#     pass

# Favor Composition over inheritance
