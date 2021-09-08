# from django.shortcuts import render
from .models import List
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListSerializer

# Create your views here.

class ListViewSet(viewsets.ModelViewSet):
    ## main query for the index route
    queryset = List.objects.all()
    ## the serializer class for serializing output
    serializer_class = ListSerializer
    ## optional permission class set permission level
    permission_classes = [permissions.AllowAny]

