from django.urls import path

from drf_demos.api.views import EmployeesListApiView, DepartmentsListApiView, DemoApiView

urlpatterns = (
    path('employees/', EmployeesListApiView.as_view(), name='api list employees'),
    path('departments/', DepartmentsListApiView.as_view(), name='api list departments'),
    path('demo/', DemoApiView.as_view(), name='demo view'),
)
