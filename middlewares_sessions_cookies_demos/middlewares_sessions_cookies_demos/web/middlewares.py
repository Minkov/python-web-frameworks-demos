import time

from django.utils.deprecation import MiddlewareMixin


class MeasureExecutionTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        request.cbm = True

    def process_response(self, request, response):
        self.end_time = time.time()
        print(f'{request.method} {request.path} executed in {self.end_time - self.start_time} seconds')
        return response


# `get_response` is a func
def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        # Before the request
        start_time = time.time()
        request.fbm = True

        result = get_response(request, *args, **kwargs)

        # After the request
        end_time = time.time()
        print(f'{request.method} {request.path} executed in {end_time - start_time} seconds')

        return result

    return middleware
