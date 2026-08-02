from rest_framework import generics

from .models import Product
from products.serializers import ProductSerializer


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
    # lookup_field = 'pk'
product_list_view = ProductDetailAPIViews