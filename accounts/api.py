from .models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, UserSerializer
from rest_framework import generics


# profile list api view
class Profile_List_Api(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# profile detail api view
class Profile_Detail_Api(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'


# user list api view
class User_List_Api(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# user detail api view
class User_Detail_Api(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'