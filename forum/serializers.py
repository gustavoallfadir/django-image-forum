from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category, Post, Reply

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
        ]

class CategorySeriealizer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta: 
        model = Post
        fields = '__all__'


class ReplySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'
        