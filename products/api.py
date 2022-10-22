from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

# product list api view
class Product_List_Api(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# product detail api view
class Product_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'