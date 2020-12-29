from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserMethod

# Create your views here.

@login_required
def my_profile_view(request):
    "View for accessing user's own profile"
    user_method = UserMethod.objects.get(id=request.user.id)
    context = {
        'user_method':user_method,
    }
    return render(request,'my_profile.html',context)
