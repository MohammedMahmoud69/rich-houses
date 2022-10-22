from .models import AboutUs
from .serializers import AboutSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# About us api view
@api_view(['GET'])
def about_api(request):
    about_api = AboutUs.objects.all()
    data = AboutSerializer(about_api , many=True).data
    return Response({'data':data})