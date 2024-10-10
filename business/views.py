from rest_framework import generics
from .models import Business
from .serializer import BusinessSerializer

# Create your views here.

class BusinessCreateListView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
