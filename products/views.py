from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_list_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        def perform_create(self, serializer):
            #serializer.save(user= self.request.user)
            #print(serializer)
            #serializer.save()
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            #or None
            if content is None:
                content = title
            serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView

class ProductDetailAPIViews(generics.RetrieveAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        # lookup_field = 'pk'
product_details_view = ProductDetailAPIViews

class ProductListAPIViews(generics.ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
product_list_view = ProductDetailAPIViews


class ProductUpdateAPIViews(generics.UpdateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        lookup_field = "pk"

        def perform_update(self, serializer):
            instance = serializer.save()
            if not instance.content:
                instance.content = instance.title  
product_update_view = ProductUpdateAPIViews.as_view()


class ProductDestroyAPIViews(generics.DestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

       # def perform_destroy(self, instance):
        #      instance
         #     super().perform_destroy()
product_delete_view = ProductDestroyAPIViews.as_view()


@api_view(["POST", "GET"])
def product_alt_view(request, pk= None, *args, **kwargs):
        method = request.method

        if method == "GET":
           if pk is not None:
                queryset = get_list_or_404(Product, pk=pk)
                data = ProductSerializer(queryset, many=True).data
                return Response(data)
           else:      
                queryset = Product.objects.all()
                data = ProductSerializer(queryset, many=True).data
                return Response(data)
        
        if method == "POST":
    
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





