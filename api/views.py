from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_home(request, *args, **kwargs):
    # request --> HttpRequest --> Django
    # print(dirs(request))
    # request.body

    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) # request.META ->
    data['content_type'] = dict(request.content_type)
    return JsonResponse(data)
