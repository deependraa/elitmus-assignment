from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'pages/index.html', context)
    # return HttpResponse('Hello world')