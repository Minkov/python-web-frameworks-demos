from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from testing_demos.web.models import Profile


class ProfilesListView(views.ListView):
    template_name = 'profiles/list.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profiles_count'] = self.object_list.count()
        context['username'] = self.request.user.username or 'Anonymous'
        context['query'] = self.request.GET.get('query')

        return context


class ProfileCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/create.html'
    success_url = reverse_lazy('list profiles')
