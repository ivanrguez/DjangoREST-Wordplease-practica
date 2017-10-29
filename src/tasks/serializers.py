# -*- coding: utf-8 -*-
from rest_framework import serializers

from tasks.models import Post


class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'titulo', 'imagen', 'intro', 'url', 'estado' ,'created_at')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class BlogsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','titulo', 'imagen', 'estado')