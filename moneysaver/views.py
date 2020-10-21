from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_overview(request):

    api_urls = {
        'API': '/api',
        'ADMIN': '/admin',
    }

    return Response(api_urls)