# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Post
from tasks.permissions import TasksPermission
from tasks.serializers import TaskSerializer, TasksListSerializer



class TaskViewSet(ModelViewSet):
    """
    Lists (GET) and creates (POST) Tasks
    """
    queryset = Post.objects.all()
    permission_classes = (TasksPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name")
    ordering_fields = ("name")

    def get_serializer_class(self):
        return TasksListSerializer if self.action == 'list' else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
