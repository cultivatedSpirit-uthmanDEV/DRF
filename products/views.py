from rest_framework import generics

from .models import Product
from products.serializers import ProductSerializer

class ProductDetailAPIViews(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
product_details_view = ProductDetailAPIViews