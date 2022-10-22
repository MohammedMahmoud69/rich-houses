from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order

# order list api view
class Order_List_Api(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# order detail api view
class Order_Detail_Api(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'