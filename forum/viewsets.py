from rest_framework import viewsets

from .serializers import CategorySeriealizer, PostSerializer, ReplySerializer
from .models import Category, Post, Reply

from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySeriealizer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all().order_by('-created')
    serializer_class = ReplySerializer