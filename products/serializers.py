from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only= True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',
    lookup_field = 'pk')
    # Email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

        """ 
            def create(self, validated_data):
            # Email = validated_data.pop('Email')
                obj = super().create(validated_data)
                #print(Email, obj)
                return obj
            def get_edit_url(self, obj):
                #return f"/api/products/{obj.pk}/"
                request = self.context.get('request')
                if request is None:
                return None
                return reverse("product-edit", kwargs= {"pk" : obj.pk}, request=request) """

    def update(self, instance, validated_data):
        email = validated_data.pop
        instance.title = validated_data.get('title')
        return instance
    
    def get_my_discount(self, obj):
        try:
           return obj.get_discount()
        except:
            return None