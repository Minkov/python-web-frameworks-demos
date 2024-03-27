from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tests_demos.web.urls")),
]

'''
# Testing
- Manual testing
    - Done by Manual QA/tester
- Automated testing
    - Done by Software developer
        - Unit testing:
            - Easy to write
            - Execution is very fast (~0.01 ms)
            - Can be many in number
        - Integration testing
            - More usable
            - Harder to write
            - Execution is slower (> 0.5 ms)
            - Less in number
    - Done by Automation QA
        - End-to-end testing
        - Functional testing
        - API testing
    - Done by ...
        - System testing
        - Performance testing
    - ....
'''
