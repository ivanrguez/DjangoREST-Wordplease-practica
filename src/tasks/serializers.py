# -*- coding: utf-8 -*-
from rest_framework import serializers

from tasks.models import Post


class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','titulo', 'imagen', 'intro', 'url', 'created_at')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'