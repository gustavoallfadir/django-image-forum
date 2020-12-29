from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from .views import home_view, logout_view, SignUpView, cat_view, UserCreatedView
from .views import flag_object_view, full_size_img_view, about_view
from .views import PostCreateView, rules, thread_view, ReplyCreateView, ReplyToReplyCreateView

from .viewsets import CategoryViewSet, PostViewSet, ReplyViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'posts',PostViewSet)
router.register(r'replies',ReplyViewSet)



urlpatterns = [
    path('',home_view ,name='home'),

    path('home/',home_view,name='home'),

    path('about/',about_view,name='about'),

    path('logout/',logout_view,name='logout'),

    path('signup',SignUpView.as_view(),name='signup'),

    path('created/',UserCreatedView.as_view(), name='user created'),

    path('category/<cat>', cat_view,name='category'),

    path('create/',login_required(PostCreateView.as_view()),name='create post'),

    path('flag_object/<obj>/<int:pk>/<path:origin>/', flag_object_view,name='flag post'),

    path('image/<obj>/<int:pk>/', full_size_img_view, name='full size img'),

    path('rules/',rules,name='rules'),

    path('thread/<thread>', thread_view, name='thread'),

    path('reply/<parent>',ReplyCreateView.as_view(),name='reply'),

    path('reply2reply/<parent>',ReplyToReplyCreateView.as_view(),name='reply to reply'),

    path('api/',include(router.urls)),
    
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]