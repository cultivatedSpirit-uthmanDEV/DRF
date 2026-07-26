from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serilizers import ProductSerializer
# Create your views here.

@api_view(["GET"])
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


    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
       """ data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        """
         #data = model_to_dict(instance, fields=['id', 'title','price', 'sale_price'])
       data = ProductSerializer(instance).data

        # model instance (model_Data)
        # turn a python dict
        # return JSON to my client
        #return JsonResponse(data)
    return Response(data)



"""
Welcome to the Django Rest Framework
Tools we are using
Setup Python Virtual Environment, Install Req, and Start Django
Creating a Python API Client
Run Django Project
Create your first API View
Echo GET Data
Django Model Instance as API Response
"""
"Next topic : DJango Model instance to dictionary"
"Next topic : Rest Framwwork View and response"
"Next topic : Django Rest Framework Modle Serilizers"
"Next topic : Ingest Data with Django Rest Framework views"