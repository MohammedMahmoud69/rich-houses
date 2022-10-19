from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class Product_List_Api(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'