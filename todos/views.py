from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todos.pagination import CustomPageNumberPagination
from .models import Todo
from todos.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import permissions, filters 

# Create your views here.
class TodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['id', 'title', 'description', 'is_complete'] #For retrivingin data through the listed fields

    search_fields = ['id', 'title', 'description', 'is_complete']
    #for searching for data through the listed fields

    ordering_fields = ['id', 'title', 'description', 'is_complete'] #for ordering data through the listed fields

    pagination_class = CustomPageNumberPagination


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)




