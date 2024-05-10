from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'message' : 'Welcome to Moments API. Create an account or login to get started.'
    })