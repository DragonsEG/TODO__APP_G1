from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset =ToDo.objects.all()
    serializer_class = ToDoSerializer
    
    



