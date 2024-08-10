from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"index.html")

def user_Response(request):
    user_message=request.GET.get('user_message')
    return HttpResponse(user_message)