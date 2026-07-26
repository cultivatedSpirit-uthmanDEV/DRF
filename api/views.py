from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
# Create your views here.

def api_home(request, *args, **kwargs):
    """"
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
    """


    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

        # model instance (model_Data)
        # turn a python dict
        # return JSON to my client
    return JsonResponse(data)




"Next topic : DJango Model instance as an API response"