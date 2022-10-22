from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics

# message list api view
class Message_List_Api(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# message detail api view
class Message_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'

