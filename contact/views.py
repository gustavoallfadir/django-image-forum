from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Message
# Create your views here.

class MessageCreateView(CreateView):

    model = Message
    template_name = 'contact.html'
    success_url = reverse_lazy('message sent')
    fields = [
        'remitent',
        'subject',
        'message',
        'img',
    ]


def message_sent(request):

    return render(request,'succes.html',{})