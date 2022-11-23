from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = 'index.html'
