from rest_framework import serializers

from apps.orders.models import Order, OrderLine
from apps.products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name','code','price']


