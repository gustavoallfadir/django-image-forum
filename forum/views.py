from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User

from .models import Category, Post, Rule, Reply, ReplyToReply
# Create your views here.


def home_view(request):
    categories = Category.objects.all().order_by('name')
    recent = Post.objects.order_by('-created')[:30]
    context = {
        'categories':categories,
        'recent':recent,
    }
    return render(request,'index.html',context=context)


def about_view(request):
    return render(request,'about.html',{})


def logout_view(request):
    logout(request)

    return reverse_lazy('home')


class SignUpView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('user created')
    template_name = 'registration/signup.html'


class UserCreatedView(LoginView):

    template_name = 'registration/user_created.html'
    success_url = reverse_lazy('home')


def cat_view(request, cat):

    posts = Post.objects.filter(category__name=cat).order_by('-created')
    categories = Category.objects.all().order_by('name')
    cat = get_object_or_404(Category,name=cat)

    context = {
        'cat':cat,
        'posts':posts,
        'categories':categories,
    }

    return render(request,'category.html',context)


class PostCreateView(CreateView):

    model = Post
    template_name = 'create_post.html'
    fields = [
        'category',
        'title',
        'content',
        'img',
    ]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


def rules(request):

    rules = Rule.objects.all()

    return render(request,'rules.html',{'rules':rules})


def thread_view(request,thread):
    parent = get_object_or_404(Post,pk=thread)
    replies = Reply.objects.filter(parent=thread).order_by('created')
    categories = Category.objects.all().order_by('name')


    context = {
        'parent':parent,
        'replies':replies,
        'categories':categories,
    }

    return render(request,'thread.html',context)


class ReplyCreateView(CreateView):

    model = Reply
    template_name = 'reply.html'
    fields = [
        'content',
        'img',
    ]
    success_url = None

    def get_success_url(self):
        return reverse_lazy('thread', kwargs = {'thread':self.kwargs.get('parent')})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.parent_id = self.kwargs.get('parent')
        return super(ReplyCreateView, self).form_valid(form)


class ReplyToReplyCreateView(CreateView):

    model = ReplyToReply
    template_name = 'reply_to_reply.html'
    fields = ['content']
    success_url = None

    def get_success_url(self):
        parent = Reply.objects.get(pk=self.kwargs.get('parent'))

        return reverse_lazy('thread',kwargs = {'thread':parent.parent.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.parent_id = self.kwargs.get('parent')
        return super(ReplyToReplyCreateView, self).form_valid(form)


def flag_object_view(request,obj,pk,origin):
    "vista para reportar un post"

    if obj=='post':
        post = get_object_or_404(Post,pk=pk)
        post.is_flagged = True
        post.save()
    
    elif obj=='reply':
        reply = get_object_or_404(Reply, pk=pk)
        reply.is_flagged = True
        reply.save()

    return redirect(origin)


def full_size_img_view(request,obj,pk):
    "Vista de imagenes en tamaño completo"

    if obj=='post':
        post = get_object_or_404(Post,pk=pk)
        context = {'object':post}

    elif obj=='reply':
        reply = get_object_or_404(Reply, pk=pk)
        context = {'object':reply}

    return render(request, 'full_size_img.html',context=context)