from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog

# Blog list api view

class Blog_List_Api(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Blog detail api view
class Blog_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
        queryset = Blog.objects.all()
        serializer_class = BlogSerializer
        lookup_field = 'id'