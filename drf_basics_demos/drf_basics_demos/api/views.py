import time

from django.shortcuts import render, redirect
from rest_framework import serializers, status, permissions
from rest_framework.decorators import api_view
from rest_framework import generics as api_generic_views

from django.views import generic as views
from rest_framework import views as api_views

from rest_framework.response import Response

from drf_basics_demos.api.models import Book


# class BookListApiView()

def list_books(request):
    book_list = Book.objects.all()

    context = {
        "book_list": book_list,
    }

    return render(request, "...", context)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("pk", "title", "author", "genre")


@api_view(http_method_names=("GET",))
def api_list_books(request):
    book_list = Book.objects.all()

    serializer = BookSerializer(book_list, many=True)

    json = serializer.data

    return Response(data=json)


class BookListView(views.View):
    def get(self, request):
        return render(request, "")

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('...')

        return render(request, "...", context=None)


class BookListApiView(api_views.APIView):
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer

    def get(self, request):
        time.sleep(3)
        book_list = Book.objects.all()
        serializer = BookSerializer(book_list, many=True)
        json = serializer.data
        return Response(data=json)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookUpdateApiView(api_views.APIView):
    def get_object(self, pk):
        return (Book.objects.filter(pk=pk)
                .first())

    def get(self, request, pk):
        serializer = BookSerializer(instance=self.get_object(pk))
        json = serializer.data
        return Response(data=json)

    def put(self, request, pk):
        serializer = BookSerializer(data=request.data, instance=self.get_object(pk))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
