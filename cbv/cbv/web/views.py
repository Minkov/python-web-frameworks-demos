from django import forms
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from cbv.web.models import Employee


def index(request):
    context = {
        'title': 'FBV',
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Bare View',
        }

        return render(request, 'index.html', context)

    def post(self, request):
        pass

    # In Django Rest Framework
    # def put(self, request):
    #     pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template view'}  # static context

    # Dynamic context
    def get_context_data(self, **kwargs):
        # Get `super`'s context
        context = super().get_context_data(**kwargs)

        # Add specific view stuff, one or more
        context['employees'] = Employee.objects.all()
        # context['form'] = MyForm()

        # Return the ready-to-use context
        return context


class IndexViewWithListView(views.ListView):
    context_object_name = 'employees'  # renames `object_list` to `employees`
    model = Employee
    template_name = 'index.html'  # web/employee_list.html
    extra_context = {'title': 'List view'}  # static context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern)

        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class EmployeeDetailsView(views.DetailView):
    context_object_name = 'employee'  # renames `object` to `employee`
    model = Employee
    template_name = 'employees/details.html'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name:',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name:',
                }
            )
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    model = Employee
    fields = '__all__'

    # Static `success_url`
    # success_url = '/'

    # Dynamic
    def get_success_url(self):
        return reverse_lazy('employee details', kwargs={
            'pk': self.object.pk,
        })

    # Replace automatic form
    # form_class = EmployeeCreateForm

    # Change the automatic form
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['placeholder'] = 'Enter ' + name
    #
    #     return form


#
#
# class RedirectToDetailsMixin:
#     url_name = None
#
#     def get_url_kwargs(self):
#         return {}
#
#     def get_success_url(self):
#         return reverse_lazy(
#             self.url_name,
#             kwargs=self.get_url_kwargs(),
#         )
#
#
# class EmployeeUpdateView(RedirectToDetailsMixin, views.UpdateView):
#     model = Employee
#     fields = '__all__'
#     template_name = 'employees/create.html'
#     url_name = 'employee details'
#
#     def get_url_kwargs(self):
#         return {
#             'pk': self.object.pk,
#         }


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/edit.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        # if the employee to update is the same as the user logged in => continue
        return super().dispatch(request, *args, **kwargs)

        # else, 401 authorized

    # def get_success_url(self):
    #     result = reverse('employee details', kwargs={
    #         'pk': self.object.pk,
    #     })
    #
    #     return result


# Employee.objects.filter(pk=pk) \


#         .get()

# def my_view(request):
#     handler = None
#     if request.method == 'GET':
#         handler = self.get
#     else:
#         handler = self.post
#     return handler()

#
# class IndexView:
#     def __init__(self):
#         self.values = [
#             random.randint(1, 15),
#         ]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It works!: {self.values}')
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))


def view(request):
    return HttpResponse('It works!')
