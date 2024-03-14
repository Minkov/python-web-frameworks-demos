import time

from django.http import JsonResponse
from django.shortcuts import render

from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = "web/index.html"

    # def get_context_data(self, **kwargs):
    #     time.sleep(3)
    #     return super().get_context_data(**kwargs)
