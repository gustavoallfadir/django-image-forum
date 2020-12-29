from django.shortcuts import render


def error_404(request,exception):
        context = {}
        return render(request,'error_404.html', context)

def error_500(request):
        context = {}
        return render(request,'error_500.html', context)