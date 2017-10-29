# -*- coding: utf-8 -*-
from rest_framework.exceptions import NotAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from tasks.models import Post
from tasks.permissions import TasksPermission
from tasks.serializers import TaskSerializer, TasksListSerializer, BlogsListSerializer


class TaskViewSet(ModelViewSet):
    """
    Lists (GET) and creates (POST) Tasks
    """
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("user")
    ordering_fields = ("titulo")

    def get_serializer_class(self):
        return TasksListSerializer if self.action == 'list' else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.order_by('-created_at')
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("user")
    ordering_fields = ("titulo")
    def get_serializer_class(self):
        return BlogsListSerializer if self.action == 'list' else TaskSerializer
