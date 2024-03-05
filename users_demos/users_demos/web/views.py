from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.forms import formset_factory
from django.http import HttpResponse

from django.views import generic as views


def index(request):
    print(request.user)  # Instance of either `User` or `AnonymousUser`
    return HttpResponse("It works")


@login_required
def about(request):
    return HttpResponse(f"It's about that, {request.user}!")


def my_view(request):
    extra = request.GET.get('forms_count', 1)
    MyFormset = formset_factory(MyForm, extra=extra)
    MyFormset(request.POST)


class TeamView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f"{request.user}'s team!")
