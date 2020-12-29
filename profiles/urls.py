from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import my_profile_view


urlpatterns = [   
    path('my_profile/', my_profile_view, name='my profile'),

]