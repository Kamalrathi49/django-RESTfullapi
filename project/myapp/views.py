from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class API_objects(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer