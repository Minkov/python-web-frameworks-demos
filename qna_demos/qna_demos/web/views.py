from django.forms import modelform_factory
from django.shortcuts import render

from django.views import generic as views

from qna_demos.api.models import Todo


def get_item_from_request(request):
    return request.POST.get("item")


TodoCreateForm = modelform_factory(Todo, fields=["title", "description", "image"])


class IndexView(views.ListView):
    queryset = Todo.objects.all()
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_todo_form"] = TodoCreateForm()
        return context


class CreateTodoView(views.CreateView):
    queryset = Todo.objects.all()
    form_class = TodoCreateForm


def add_item_to_cart(request):
    item = get_item_from_request(request)

    # Add item to cart
    session_cart = request.session.get("cart", [])
    session_cart.append(item)
    request.session["cart"] = session_cart

    # ...
