from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import MessageCreateView, message_sent

urlpatterns = [
    path('',MessageCreateView.as_view(),name='contact'),

    path('sent/',message_sent,name='message sent'),
]