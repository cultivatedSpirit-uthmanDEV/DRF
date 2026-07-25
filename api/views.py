from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
    return JsonResponse({"Message": "Hi there, This is my first Django API response"})
