from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["POST"])
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


    """instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:"""
    """ First way of changing data to naitive python : data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        """
         #Here is the data = model_to_dict(instance, fields=['id', 'title','price', 'sale_price'])
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
       # instance = serializer.save()
        print(serializer.data)
        data = serializer.data
    return Response(data)

        # model instance (model_Data)
        # turn a python dict
        # return JSON to my client
        #return JsonResponse(data)
    return Response(data)




