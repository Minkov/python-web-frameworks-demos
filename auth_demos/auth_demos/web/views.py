from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as views
from auth_demos.web.models import Model1


def index(request):
    param = 1  # From request

    # # No possible SQL injection
    # model1_list = list(Model1.objects.all() \
    #                    .filter(pk=param))
    #
    # # Possible SQL injection
    # model1_list2 = list(Model1.objects.raw(f"SELECT * FROM web_model1 WHERE id = {param}"))
    #
    # # No possible SQL injection
    # model1_list3 = list(Model1.objects.raw("SELECT * FROM web_model1 WHERE id = param", params={"id": param}))
    context = {
        'model1_list': Model1.objects.all(),
    }
    return render(request, "index.html", context)


def private_view(request):
    return HttpResponse("View Accessed")


Model1GetForm = modelform_factory(Model1, fields=("title"))
Model1PostForm = modelform_factory(Model1, fields=("title"))


class CreateModel1View(views.CreateView):
    form_get_class = Model1GetForm
    form_post_class = Model1PostForm

    def get_form_class(self):
        if self.request.method == "GET":
            return self.form_get_class
        return self.form_post_class
